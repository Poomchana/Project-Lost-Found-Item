from datetime import datetime
from .extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    item_type = db.Column(db.String(10))  # lost / found
    status = db.Column(db.String(20), default="open")
    location = db.Column(db.String(200))
    date_reported = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))

class ItemImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey("item.id"))
    image_url = db.Column(db.String(255))

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lost_item_id = db.Column(db.Integer, db.ForeignKey("item.id"))
    found_item_id = db.Column(db.Integer, db.ForeignKey("item.id"))
    score = db.Column(db.Float)
    status = db.Column(db.String(20), default="pending")

class Claim(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    match_id = db.Column(db.Integer, db.ForeignKey("match.id"))
    meet_place = db.Column(db.String(200))
    meet_time = db.Column(db.DateTime)
    status = db.Column(db.String(20), default="scheduled")
