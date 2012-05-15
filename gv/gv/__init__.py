from flask.app import Flask

from gv import views

__author__ = 'Administrator'

#默认的应用名称
DEFAULT_APP_NAME = "gv"



def create_app():
    app = Flask(DEFAULT_APP_NAME)
    app.register_module(views.frontend, url_prefix="")
    app.register_module(views.admin,url_prefix="/admin")
    return app

