# -*- coding:utf-8 -*-

#import flask

#from flask import Flask

#print flask.__version__

#import jinja2
#print jinja2.__version__
import datetime

from flask import Flask
from flaskext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 数据库配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:eeeeeeee@localhost/pywebdb';
#生成db对象
db = SQLAlchemy(app)

#用户模型
class User(db.Model):
    __tablename__ = 'fk_user'
    #自增编号
    id = db.Column(db.Integer,primary_key=True)
    nick = db.Column(db.String(50),unique=True)
    email = db.Column(db.String(50),unique=True)

    def __init__(self,nick,email):
        self.nick = nick
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.nick

class Post(db.Model):
    __tablename__ = 'fk_post'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)

    category_id = db.Column(db.Integer,db.ForeignKey('fk_category.id'))
    category = db.relationship('Category',backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, title, body, category, pub_date=None):
        self.title = title
        self.body = body
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date
        self.category = category

    def __repr__(self):
        return '<Post %r>' % self.title


class Category(db.Model):
    __tablename__ = 'fk_category'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(50))

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name


# 新建或生成所有模型数据表
db.drop_all();
db.create_all()

#添加

user = User('test','test@test.com')
user1 = User('test1','test1@test.com')

db.session.add(user)
db.session.add(user1)
db.session.commit()

#查找
users = User.query.all()
for u in users :
    print u
print users

users = User.query.order_by('id desc')
for u in users:
    print u

user = User.query.filter_by(nick = 'test').first()
print user.id,user.email

db.session.delete(user)
db.session.commit()

users = User.query.all()
print len(users)

print User.query.limit(1).all()
user =  User.query.get(2)
print user
user.nick = 'update test1'
db.session.commit()
user2 = User.query.get(2)
print user2