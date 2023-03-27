from flask import Blueprint, request, make_response, jsonify
from src.extension.extension import db
from src.modal.user import Users
from werkzeug.security import generate_password_hash


user_blueprint = Blueprint("users", __name__)


@user_blueprint.route('/')
def health_check():
    return make_response(jsonify({"status": "true", "message": "success"})), 200


@user_blueprint.route('/create-user', methods=["POST"])
def create_user():
    try:
        db.create_all()

        data = request.get_json()

        user = Users.query.filter_by(email=data['email']).first()

        if user is not None:
            return make_response(jsonify({"status": "true", "message": "user already exist"})), 200

        hashed_password = generate_password_hash(data['password'])

        user = Users(
            username=data['username'],
            password=hashed_password,
            email=data['email'],
            role='user',
            mobileno=data['mobileno']
        )

        db.session.add(user)
        db.session.commit()

        return make_response(jsonify({"status": True, "message": "Successfully Registered!!!"})), 200
    except Exception as e:
        return make_response(jsonify({"status": False, "message": e})), 501


@user_blueprint.route('/users', methods=["GET"])
def get_all_user():
    try:

        users = db.session.query(Users).all()
        if users is not None:
            user_list = [
                {"username": user.username,
                 "email": user.email,
                 "mobil_no": user.mobileno
                 } for user in users
            ]
        return make_response(jsonify({"status": "true", "data": user_list})), 200
    except Exception as e:
        return make_response(jsonify({"status": "false", "message": e})), 501
