# -*- coding:utf-8
__author__ = 'window2003@gmail.com'

from couchdbkit import *

import datetime

from couchdbkit import *

class Greeting(Document):
    author = StringProperty()
    content = StringProperty()
    date = DateTimeProperty()
#
#    # server object
server = Server()
#
## create database
db = server.get_or_create_db("greeting")
#
#
#
## associate Greeting to the db
Greeting.set_db(db)
#
# create a new greet
greet = Greeting(
    author="Benoit",
    content="Welcome to couchdbkit world",
    date=datetime.datetime.utcnow()
)

# 第一次是添加
greet.save()


#取出一个
greet = Greeting.get('679bdea0842287e294fc1920045d2b5c')
#
print greet['author']
print greet.content
print greet._rev
#修改
greet.author = 'abdcfdd'
greet.save()

print greet['author']
print greet.content
print greet._rev
#删除
greet.delete()


