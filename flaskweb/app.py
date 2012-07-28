# -*- coding:utf-8 -*-
__author__ = 'ajaxj@qq.com'

from flask import Flask,url_for,render_template

app = Flask(__name__)
app.debug = True

#@app.route('/')
#def home():
#    return 'home index page'

@app.route('/')
def index():
    app.logger.debug("this is debug")
    app.logger.warning('this is warning')
    app.logger.error('this is error')
    return render_template('index.html')

@app.route('/login')
def login():pass

@app.route('/user/<username>')
def profile(username):pass

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

with app.test_request_context():
    print url_for('index')
    print url_for('login')
    print url_for('login',next='/')
    print url_for('profile',username='jon')



if __name__ == '__main__':
    app.run()