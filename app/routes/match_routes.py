from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from ..extensions import db
from ..models import Match, Item
from ..services.matching_service import simple_candidates_for_lost

match_bp = Blueprint("match_bp", __name__)

@match_bp.get("/candidates/<int:lost_item_id>")
@jwt_required()
def candidates(lost_item_id):
    lost = db.session.get(Item, lost_item_id)
    if not lost or lost.item_type!="lost":
        return jsonify({"error":"lost item not found"}), 404
    cands = simple_candidates_for_lost(lost_item_id)
    return jsonify([{
        "found_item_id": it.id,
        "title": it.title,
        "score": score
    } for it, score in cands])

@match_bp.post("")
@jwt_required()
def create_match():
    data = request.get_json()
    m = Match(lost_item_id=data["lost_item_id"], found_item_id=data["found_item_id"], score=data.get("score",0.0))
    db.session.add(m); db.session.commit()
    return jsonify({"id": m.id}), 201

@match_bp.patch("/<int:match_id>/status")
@jwt_required()
def update_status(match_id):
    m = db.session.get(Match, match_id)
    if not m: return jsonify({"error":"not found"}), 404
    m.status = request.get_json().get("status","pending")
    db.session.commit()
    return jsonify({"ok": True})
