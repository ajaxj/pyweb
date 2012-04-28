# -*- coding:utf-8 -*-
# couchdb simples
import couchdb

SERVER = 'http://localhost:5984'

couch = couchdb.Server(SERVER)

db = couch.create('test')
#db = couch['test']
#doc = {'foo':'bar'}
#db.save(doc)

for id in db:
    db.delete(db[id])

for id in db:
    print id

couch.delete('test')
