import os
import logging
import datetime

from logging.handlers import  RotatingFileHandler


from flask import Flask, g, session, request, flash, redirect, jsonify, url_for
from fkapp import views
from fkapp.extensions import couchdb


DEFAULT_APP_NAME = 'fkapp'

DEFAULT_MODULES = (
    (views.frontend, ""),
    (views.admin, "/admin"),
 )

def create_app(config=None, modules=None):

    if modules is None:
        modules = DEFAULT_MODULES

    app = Flask(DEFAULT_APP_NAME)

    # config
    app.config.from_pyfile(config)

#    app.config['COUCHDB_DATABASE'] = 'mydb'

    configure_extensions(app)

    configure_logging(app)

    # register module
    configure_modules(app, modules)

    return app




def configure_extensions(app):
    # configure extensions
    couchdb.init_app(app)





def configure_modules(app, modules):

    for module, url_prefix in modules:
        app.register_module(module, url_prefix=url_prefix)


def configure_logging(app):

    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]')

    debug_log = os.path.join(app.root_path,
        app.config['DEBUG_LOG'])

    debug_file_handler =\
    RotatingFileHandler(debug_log,
        maxBytes=100000,
        backupCount=10)

    debug_file_handler.setLevel(logging.DEBUG)
    debug_file_handler.setFormatter(formatter)
    app.logger.addHandler(debug_file_handler)

    error_log = os.path.join(app.root_path,
        app.config['ERROR_LOG'])

    error_file_handler =\
    RotatingFileHandler(error_log,
        maxBytes=100000,
        backupCount=10)

    error_file_handler.setLevel(logging.ERROR)
    error_file_handler.setFormatter(formatter)
    app.logger.addHandler(error_file_handler)
