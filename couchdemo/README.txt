一些包

http://couchdbkit.org/docs/django-extension.html

http://code.google.com/p/couchdb-python/
使用couchdb-python的例子:
http://www.shaxiaozi.com/log/tag/python



http://packages.python.org/Flask-CouchDBKit/
http://pypi.python.org/pypi/Flask-CouchDBKit


- 显示引用文字 -
greet.get('someid')
greet.author = 'updated author"
greet.save()


or use client.*

doc =  db.get("someid")
doc['autho'] = 'new author'
db.save_doc(doc)
doc['author'] = 'updated author 2'
db.save_doc(doc)
- benoit


flask-couchdb
http://packages.python.org/Flask-CouchDB/
https://gist.github.com/1277655
http://blog.mathieu-leplatre.info/une-demo-squelettique-de-python-flask-couchdb-fr.html