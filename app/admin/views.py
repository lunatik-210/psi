from flask import render_template

def hello_world():
    return render_template('admin.html')
