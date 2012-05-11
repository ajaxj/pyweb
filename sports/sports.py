# -*- coding:utf-8
import re
import urllib2
# TODO A
import  logging

from flask import Flask,render_template


__author__ = 'window2003@gmail.com'

app = Flask(__name__)
app.config.from_pyfile('defaults.cfg')
app.config.from_pyfile('local.cfg')
app.debug = True
# TODO A

if app.debug:
    logging.basicConfig(level=logging.DEBUG)
else:
    # TODO 用邮件发送LOG
    print 'email to logging error'



################## function ###############
def show_listing(template):
    return render_template(template)



@app.route('/',defaults={'page':1})
@app.route('/page/<int:page>')
def show_all(page):
    print page
    return show_listing('show_all.html')


if __name__ == '__main__':
    app.run()
