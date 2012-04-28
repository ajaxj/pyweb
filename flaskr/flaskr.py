# -*- coding:utf-8 -*-
from __future__ import with_statement
from sqlite3 import dbapi2 as sqlite3
from contextlib import closing
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash


import logging



DATABASE = 'flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


file_handler = logging.FileHandler('flaskr.log')

file_handler.setLevel(logging.DEBUG)
log_formatter = logging.Formatter('''
Message type:       %(levelname)s
Location:           %(pathname)s:%(lineno)d
Module:             %(module)s
Function:           %(funcName)s
Time:               %(asctime)s
Message:			%(message)s
''')
file_handler.setFormatter(log_formatter)
app.logger.addHandler(file_handler)

def connect_db():
    """Returns a new connection to the database."""
    return sqlite3.connect(app.config['DATABASE'])

#初始数据库
def init_db():
    """Creates the database tables."""
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.before_request
def before_request():
	g.db = connect_db()

@app.after_request
def after_request(response):
	g.db.close()
	return response


@app.route('/')
def show_entries():
	#app.logger.debug('A value for debugging')
	#app.logger.warning('A warning occurred (%d apples)', 42)
	#app.logger.error('An error occurred')
	cur = g.db.execute('select title,text from entries order by id desc')
	entries = [dict(title=row[0],text=row[1]) for row in cur.fetchall()]
	return render_template('show_entries.html',entries = entries)


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (title, text) values (?, ?)',
                 [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))



@app.route('/login',methods=['GET','POST'])
def login():
	#出错提示
	error = None
	# request.path == '/login' request.path得到当前的请求路径
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME']:
			error = "username error"
		elif request.form['password'] != app.config['PASSWORD']:
			error = "password error"
		else:
			session['logged_in'] = True
			flash('You were logged in')
			return redirect(url_for('show_entries'))

	return render_template('login.html',error=error)


# 跳到401的错误
@app.route('/testerr')
def testerr():
	abort(401)

# 404 查无此页的自定义方式
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))




if __name__ == '__main__':
	#初始数据库
	#init_db()
	app.run()
