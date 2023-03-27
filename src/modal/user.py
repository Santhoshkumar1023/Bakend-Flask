import datetime

from src.extension.extension import db


class Users(db.Model):
    __tablename__ = 'users'

    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(100), primary_key=True,
                      nullable=False, unique=True)
    role = db.Column(db.String(100), nullable=False)
    mobileno = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, username, password, email, role, mobileno):
        self.username = username
        self.password = password
        self.email = email
        self.role = role
        self.mobileno = mobileno
        self.created_at = datetime.datetime.now()
