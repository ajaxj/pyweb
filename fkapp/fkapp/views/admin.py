from flask import Module,render_template


__author__ = 'Administrator'


admin = Module(__name__)

@admin.route("/")
def index():
    return render_template('admin/index.html')


