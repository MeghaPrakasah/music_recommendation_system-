from enum import unique
from ssl import _create_unverified_context
from song_recc import db,app,login_manager
from flask_login import UserMixin
from flask_table import Table, Col, LinkCol
# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

@login_manager.user_loader
def load_user(id):
    return Login.query.get(int(id))



class Login(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80), nullable=False)
    usertype = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(200))
    contact = db.Column(db.String(200))



class Teachers(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80), nullable=False)
    usertype = db.Column(db.String(80))
    name = db.Column(db.String(200))
    clas = db.Column(db.String(200))
    subject = db.Column(db.String(200))
    division = db.Column(db.String(200))
    contact = db.Column(db.String(200))


class Students(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    name = db.Column(db.String(200))
    clas = db.Column(db.String(200))
    division = db.Column(db.String(200))
    contact = db.Column(db.String(200))
    sid = db.Column(db.String(200))


class Detection(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    sid = db.Column(db.Integer)
    subject = db.Column(db.String(80))
    emotion = db.Column(db.String(80))
    det_date = db.Column(db.String(80))
    time = db.Column(db.String(80))








    
  
