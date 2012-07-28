# -*- coding:utf-8 -*-
from flask import Flask
from mysite.views import frontend, admin
from mysite.extensions import db


__author__ = 'window2003@gmail.com'

DEFAULT_APP_NAME = 'mysite'

DEFAULT_MODULES = (
    (frontend, ""),
    (admin, "/admin"),
)

def create_app(config=None, modules=None):
    if modules is None:
        modules = DEFAULT_MODULES
    app = Flask(DEFAULT_APP_NAME)

    # config
    app.config.from_pyfile(config)

    configure_extensions(app)

    configure_modules(app, modules)
    return app


def configure_extensions(app):
    # configure extensions
    db.init_app(app)


def configure_modules(app, modules):
    for module, url_prefix in modules:
        app.register_module(module, url_prefix=url_prefix)
