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
    phone = db.Column(db.String(45))
    passwd = db.Column(db.String(45))
    logintype = db.Column(db.String(45))

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)

    def __repr__(self):
        return "<%s>" % self.email


#球场
class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)

    def __repr__(self):
        return "<%s>" % self.name


#球队
class Team(db.Model):
    __tablename__ = 'teams'
    id = db.Colmun(db.Integer,primary_key = True)
    name = db.Column(db.String(45))

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)

    def __repr__(self):
        return "<%s>" % self.name


# 比赛
class Match(db.Model):
    __tablename__ = 'matchs'
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.String(45))

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)

    def __repr__(self):
        return "<%s>" % self.name







