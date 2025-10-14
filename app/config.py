import os
from datetime import timedelta

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "devjwt")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=3)
    CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*").split(",")

config = {"development": Config, "production": Config}
