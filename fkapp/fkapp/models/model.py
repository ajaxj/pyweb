# -*- coding:utf-8
from fkapp.extensions import db

__author__ = 'Administrator'


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


#hakuzy原生表
class Hakuzy(db.Model):
    __tablename__ = 'mv_movie_hakuzy'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(200))
    url = db.Column(db.String(200))
    category = db.Column(db.String(200))

    def __init__(self,title,url):
        self.title = title
        self.url = url

    def __repr__(self):
        return '<mv %r' % self.title
