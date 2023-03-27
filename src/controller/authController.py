from werkzeug.security import check_password_hash
from flask import Blueprint, make_response, jsonify, request
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
            return make_response(jsonify({"message": "success"})), 200
        return make_response(jsonify({"status": "false", "message": "user not exist"}))
        # return make_response(jsonify({"mesage": "not signed up"}))
    except Exception as e:
        return make_response(jsonify({"message": e}))
