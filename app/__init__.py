from flask import Flask, jsonify
from .extensions import db, jwt, cors
from .models import *
from .routes.auth_routes import auth_bp
from .routes.item_routes import item_bp

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///lostfound.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = "supersecretkey"

    db.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(item_bp, url_prefix="/api/items")

    @app.route("/")
    def index():
        return jsonify({"message": "Lost & Found API", "status": "OK"})
    return app
