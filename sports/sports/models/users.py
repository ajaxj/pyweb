#coding:utf-8
"""
数据模型
"""
import hashlib
from sports.extensions import db
from datetime import  datetime

__author__ = 'Administrator'

class User(db.Model):
    __tablename__ = 'users'

    #权限编号
    MEMBER = 100
    MODERATOR = 200
    ADMIN = 300

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=True)
    nickname = db.Column(db.String(20))
    email = db.Column(db.String(100),unique=True,nullable=False)
    _password = db.Column("password",db.String(80),nullable=False)
    role = db.Column(db.Integer,default=MEMBER)
    activation_key = db.Column(db.String(40))
    date_joined = db.Column(db.DateTime,default=datetime.utcnow)
    last_joined = db.Column(db.DateTime,default = datetime.utcnow)
    last_request = db.Column(db.DateTime,default= datetime.utcnow)
    block = db.Column(db.Boolean,default=False)

    def __init__(self,*args,**kwargs):
        super(User,self).__init__(*args,**kwargs)

    def __str__(self):
        return self.nickname

    def __repr__(self):
        return "<%s>" % self

    def _get_password(self):
        return self._password

    def _set_password(self,password):
        self._password = hashlib.md5(password).hexdigest()

    #给密码绑定一些方法
    password = db.synonym("_password",descriptor=property(_get_password,_set_password))

    #验证密码
    def check_password(self,password):
        if self.password is None:
            return False
        return self.password == hashlib.md5(password).hexdigest()

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