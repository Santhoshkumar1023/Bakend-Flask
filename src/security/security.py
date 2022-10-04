from re import U
from webbrowser import get
from src.users.users import Users

users=[
    Users(1,'santhosh','12345')
]


username_mapping = { u.username : u for u in users }
userid_mapping ={ u.id : u for u in users}

# username_mapping={
#     'user':{
#         "username":"santhoshkumar",
#         "password":"12345"
#     }
# }

# userid_mapping={
#     '1':{
#         "username":"santhoshkumar",
#         "password":"12345"
#     }
# }


def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id,None)


def authenticate(username,password):
    user= username_mapping.get(username,None)
  
    if  user and user.password == password:
        return user
