# -*- coding:utf-8
from flask.ext.sqlalchemy import SQLAlchemy

# couchdb 之前的配置
# from flaskext.couchdbkit import CouchDBKit
# __all__=['couchdb']
# couchdb = CouchDBKit()
__all__  = ['db']
db = SQLAlchemy()

