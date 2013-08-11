from flask.ext.sqlalchemy import SQLAlchemy
import logging
from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)


file_handler = logging.FileHandler('app.log')
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

import admin.views
