
from src import create_app


app = create_app()


app.run(port=5000, debug=True)


# from flask import Flask
# # from src.store.store import Store
# from flask_restful import Api
# # from flask_jwt import JWT

# # from src..security import authenticate,identity
# # from src.users.users import Users
# from src.users.users import user_bluprint


# app = Flask(__name__)


# # this is secret key when we  push to production
# # add in env
# app.secret_key = 'secretKey'

# api = Api(app)


# # path is like /auth
# # jwt = JWT(app,authenticate,identity)

# # api.add_resource(Store,'/stores')
# # api.add_resource(Users,'/users')
# # api.add_resource(Store,'/store/<string:name>')

# app.register_blueprint(user_bluprint)

# app.run(port=5000, debug=True)
