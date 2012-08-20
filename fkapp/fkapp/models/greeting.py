# -*- coding:utf-8
__author__ = 'window2003@gmail.com'


from fkapp.extensions import couchdb

class Greeting(couchdb.Document):
    author = couchdb.StringProperty()
    content = couchdb.StringProperty()
    date = couchdb.DateTimeProperty()