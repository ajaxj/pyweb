#coding:utf-8
"""
数据模型
"""
from sports.extensions import db
from datetime import  datetime

__author__ = 'Administrator'

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=True)
    nickname = db.Column(db.String(20))
    date_joined = db.Column(db.DateTime,default=datetime.utcnow)

    def __init__(self,username,nickname):
        self.username = username
        self.nickname = nickname

    def __str__(self):
        return self.nickname

    def __repr__(self):
        return "<%s>" % self
