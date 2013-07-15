# -*- coding:utf-8 -*-
from admin import db

#管理员表
class Admin(db.Model):
    __tablename__ = 'admins'
    id = db.Column(db.Integer,primary_key=True)
    adminname = db.Column(db.String(45))
    adminpass = db.Column(db.String(45))

    def __init__(self, adminname,adminpass):
        self.adminname = adminname
        self.adminpass = adminpass

    def __repr__(self):
        return '<Admin %r>' % self.adminname

#用户表
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(45))

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)

    def __repr__(self):
        return "<%s>" % self.email
