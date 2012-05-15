#coding:utf-8
"""
数据模型
"""
from sports.extensions import db
from datetime import  datetime

__author__ = 'Administrator'

class User(db.Model):
    __tablename__ = 'users'

    MEMBER = 100
    MODERATOR = 200
    ADMIN = 300

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=True)
    nickname = db.Column(db.String(20))
    email = db.Column(db.String(100),unique=True,nullable=False)
    _password = db.Column("password",db.String(80),nullable=False)
    role = db.Column(db.Integer,default=MEMBER)
    date_joined = db.Column(db.DateTime,default=datetime.utcnow)

    def __init__(self,username,nickname):
        self.username = username
        self.nickname = nickname

    def __str__(self):
        return self.nickname

    def __repr__(self):
        return "<%s>" % self


class UserCode(db.Model):
    __tablename__ = 'usercode'

    id = db.Column(db.Integer,primary_key=True)
    code = db.Column(db.String(20),nullable=False)
    role = db.Column(db.Integer,default=User.MEMBER)

    def __init__(self,*args,**kwargs):
        super(UserCode,self).__init__(*args,**kwargs)

    def __str__(self):
        return self.code

    def __repr__(self):
        return "<%s>" % self