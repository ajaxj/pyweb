# -*- coding:utf-8

# 改写的model 使用 couchdbkit 产生 模型
from couchdbkit.ext.django.schema import *

class Greeting(Document):
    author = StringProperty()
    content = StringProperty(required=True)
    date = DateTimeProperty()