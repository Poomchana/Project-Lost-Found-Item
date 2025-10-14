from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..extensions import db
from ..models import Item

item_bp = Blueprint("items", __name__)

@item_bp.post("")
@jwt_required()
def add_item():
    data = request.get_json()
    new_item = Item(
        title=data["title"],
        description=data.get("description"),
        item_type=data["item_type"],
        location=data.get("location"),
        user_id=get_jwt_identity()
    )
    db.session.add(new_item)
    db.session.commit()
    return jsonify({"message": "Item added successfully"})

@item_bp.get("")
def list_items():
    q = request.args.get("q")
    item_type = request.args.get("type")
    query = Item.query
    if q:
        query = query.filter(Item.title.like(f"%{q}%"))
    if item_type:
        query = query.filter_by(item_type=item_type)
    items = query.all()
    return jsonify([{
        "id": i.id,
        "title": i.title,
        "item_type": i.item_type,
        "status": i.status,
        "location": i.location
    } for i in items])
