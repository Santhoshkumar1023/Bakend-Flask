from flask import Flask
from flask_cors import CORS
from src.extension.extension import db, jwt
from src.controller.userController import user_blueprint
from src.controller.authController import auth
from datetime import timedelta
import os


def create_app():
    app = Flask(__name__)
    # os.getenv()
    CORS(app)

    register_route(app)
    configure_app(app)
    return app


def configure_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:root@localhost:5432/postgres"
    db.init_app(app)

    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET')
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=30)
    app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=1)
    jwt.init_app(app)
    return None


def register_route(app):
    app.register_blueprint(user_blueprint)
    app.register_blueprint(auth)
    # app.register_blueprint(
    #     user_blueprint)
    return None
