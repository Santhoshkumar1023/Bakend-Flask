

from flask import request, Blueprint
from flask import jsonify,make_response,request
from src.db.db import get_db_connection

from flask.views import MethodView

import uuid

user_bluprint=Blueprint('users',__name__)

class Users(MethodView):

    # def __init__(self,_id,username,password):
    #     self.id=_id
    #     self.username=username
    #     self.password=password

    def post(self):
        print("here")
        try:
            data=request.get_json()
           
            connection = get_db_connection()
            
            cursor=connection.cursor()

            # query= "CREATE TABLE users (id serial,username VARCHAR(150),password VARCHAR(150) NOT NULL)"

            # cursor.execute(query)

           
            # my_id= str(uuid.uuid4())

            cursor.execute(("INSERT INTO users(username,password) VALUES(%s,%s)") , (data['username'],data['password']))

            connection.commit()
        
            cursor.close()

            connection.close()
            return make_response(jsonify({"message":"success"}),201)
        except Exception as e:
            return make_response(jsonify({"message":"failed","error":e}),501)
         

registration_view = Users.as_view('users')


user_bluprint.add_url_rule(
    '/users/create',
    view_func=registration_view,
    methods=['POST']
)