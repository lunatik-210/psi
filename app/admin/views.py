from flask import render_template

def hello_world():
    return render_template('admin.html')

def login():
    return render_template('login.html')