from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..extensions import db
from ..models import Conversation, Message

chat_bp = Blueprint("chat_bp", __name__)

@chat_bp.post("/conversations")
@jwt_required()
def create_conversation():
    match_id = request.get_json().get("match_id")
    conv = Conversation(match_id=match_id)
    db.session.add(conv); db.session.commit()
    return jsonify({"id": conv.id}), 201

@chat_bp.post("/messages")
@jwt_required()
def send_message():
    data = request.get_json()
    msg = Message(
        conversation_id=data["conversation_id"],
        sender_id=get_jwt_identity(),
        content=data["content"]
    )
    db.session.add(msg); db.session.commit()
    return jsonify({"id": msg.id}), 201

@chat_bp.get("/conversations/<int:conv_id>/messages")
@jwt_required()
def list_messages(conv_id):
    msgs = db.session.execute(db.select(Message).filter_by(conversation_id=conv_id).order_by(Message.created_at.asc())).scalars().all()
    return jsonify([{"id":m.id,"from":m.sender_id,"text":m.content,"at":m.created_at.isoformat()} for m in msgs])
