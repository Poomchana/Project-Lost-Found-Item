from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..extensions import db
from ..models import Claim, Match, Item

claim_bp = Blueprint("claim_bp", __name__)

@claim_bp.post("")
@jwt_required()
def create_claim():
    data = request.get_json()
    m = db.session.get(Match, data["match_id"])
    if not m: return jsonify({"error":"match not found"}), 404
    # สมมติว่าเจ้าของ lost เป็นผู้สร้างการนัด
    lost_owner_id = db.session.get(Item, m.lost_item_id).user_id
    receiver_id = db.session.get(Item, m.found_item_id).user_id
    c = Claim(
        match_id=m.id,
        claimer_user_id=lost_owner_id,
        receiver_user_id=receiver_id,
        meet_time=data.get("meet_time"),
        meet_place=data.get("meet_place"),
        note=data.get("note")
    )
    db.session.add(c); db.session.commit()
    return jsonify({"id": c.id}), 201

@claim_bp.patch("/<int:claim_id>")
@jwt_required()
def update_claim(claim_id):
    c = db.session.get(Claim, claim_id)
    if not c: return jsonify({"error":"not found"}), 404
    data = request.get_json()
    for k in ["meet_time","meet_place","note","status","proof_url"]:
        if k in data: setattr(c, k, data[k])
    db.session.commit()
    return jsonify({"ok": True})
