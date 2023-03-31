
from flask import Blueprint, make_response, jsonify, request
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required
from src.model.user import Users
from src.extension.extension import bcrypt, db
auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()

        email = data["email"]
        password = data["password"]

        user = Users.query.filter_by(email=email).first()

        print(f'{user}>>>>>>>>>>>>>>')

        if user is not None and bcrypt.check_password_hash(user.password, password):
            access_token = create_access_token(identity=email)
            refresh_token = create_refresh_token(identity=email)

            response = {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "user_data": {
                    "username": user.username,
                    "email": user.email,
                    "mobileno": user.mobileno,
                }
            }

            return make_response(jsonify({"data": response, "message": "Successfully Signedin...!", "status": True})), 200
        return make_response(jsonify({"status": "false", "message": "user not exist"}))

    except Exception as e:
        return make_response(jsonify({"message": e}))


@auth.route('/refresh-token', methods=['POST'])
@jwt_required(refresh=True)
def refreshToken():
    try:
        email = get_jwt_identity()
        access_token = create_access_token(identity=email)
        refresh_token = create_refresh_token(identity=email)
        users = Users.query.filter_by(email=email).first()
        if users is not None:
            response = {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "user_data": {
                    "username": users.username,
                    "email": users.email,
                    "mobileno": users.mobileno
                }
            }
            return make_response(jsonify({'status': True, "data": response})), 200
    except Exception as e:
        return make_response(jsonify("error", e)), 501
