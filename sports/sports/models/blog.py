#coding:utf-8
"""
post model
"""
from sports.extensions import db
from sports.models.users import User
from datetime import datetime

__author__ = 'window2003@gmail.com'

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer,primary_key = True)
    author_id = db.Column(db.Integer,db.ForeignKey(User.id,ondelete='CASCADE'),nullable=False)
    _title = db.Column("title",db.Unicode(100),index = True)
    _slug = db.Column("slug",db.Unicode(50),unique=True,index=True)
    content = db.Column(db.UnicodeText)
    num_comments = db.Column(db.Integer,default = 0)
    created_date = db.Column(db.DateTime,default = datetime.utcnow)
    update_time = db.Column(db.DateTime,default = datetime.utcnow,onupdate=datetime.utcnow)

    _tags = db.Column("tags",db.Unicode(100),index=True)

    author = db.relation(User,innerjoin=True,lazy="joined")
    # TODO mapper

    def __init__(self,*args,**kwargs):
        super(Post,self).__init__(*args,**kwargs)

    def __str__(self):
        return self.title

    def __repr__(self):
        return "<%s>" % self