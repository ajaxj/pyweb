# -*- coding:utf-8 -*-
# couchquery simple
import os
from couchquery import *
this_dir = os.path.abspath(os.path.dirname(__file__))
design_doc = os.path.join(this_dir,'views')
db = Database('http://localhost:5984/test')
db.sync_design_doc('banzai', design_doc)

def init():
    lectroids = [
            {'type':'red-lectroid', 'name':'John Whorfin'},
            {'type':'black-lectroid', 'name':'John Parker'},
            {'type':'red-lectroid', 'name':'John Bigboote'},
            {'type':'red-lectroid', 'name':"John O'Connor"},
            {'type':'red-lectroid', 'name':"John Gomez"},
            {'type':'black-lectroid', 'name':"John Emdall"},
            {'type':'red-lectroid', 'name':"John YaYa"},
            {'type':'red-lectroid', 'name':"John Small Berries"},
    ]
    for doc in lectroids:
        db.create(doc)

def test_simple_list():
    alldocs = db.views.all()
    for d in alldocs:
        print d

def test_simple_update():
    alldocs = db.views.all()
    alldocs.location = 'shanghai'
    alldocs.save()

