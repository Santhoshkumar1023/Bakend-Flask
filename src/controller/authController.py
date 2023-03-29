from werkzeug.security import check_password_hash
from flask import Blueprint, make_response, jsonify, request
from flask_jwt_extended import create_access_token, create_refresh_token
from src.modal.user import Users

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()

        email = data['email']
        password = data['password']

        user = Users.query.filter_by(email=email).first()

        if user is not None and check_password_hash(user.password, password):
            access_token = create_access_token(identity=email)
            user_data = {
                "user_name": user.username,
                "email": user.email,
                "mobileno": user.mobileno
            }
            return make_response(jsonify({"data": user_data, "access_token": access_token, "message": "Successfully Signedin...!", "status": True})), 200
        return make_response(jsonify({"status": "false", "message": "user not exist"}))
        # return make_response(jsonify({"mesage": "not signed up"}))
    except Exception as e:
        return make_response(jsonify({"message": e}))


@auth.route('/refresh-token', methods=[])
def refresh_token():
    try:

        return make_response(jsonify({'status': True})), 200
    except Exception as e:
        return make_response(jsonify("error", e)), 501
