from flask import session, request, redirect, render_template
from flask.ext.login import login_user, current_user, logout_user

from singnin_form import SigninForm
from app.models.models import User

LOGGED_IN_TOKEN = 'logged_in'


def logout():
    if current_user.is_authenticated():
        session.pop(LOGGED_IN_TOKEN)
        logout_user()
    return redirect("/")


def login():
    if request.method == 'GET':
        if current_user is not None and current_user.is_authenticated():
            return redirect("/")
        return render_template('login.html', signin_form=SigninForm())
    else:
        form = SigninForm(request.form)
        if form.validate():
            user = User.objects(user_name=form.username.data).first()
            if user is None:
                form.username.errors.append('Username not found')
                return render_template('login.html', signin_form=form)
            if user.password != form.password.data:
                form.password.errors.append('Passwords did not match')
                return render_template('login.html', signin_form=form)
            login_user(user, remember=form.remember_me.data)
            session[LOGGED_IN_TOKEN] = True
            return redirect("admin")
        return render_template('login.html', signin_form=form)
        # # if bcrypt.check_password_hash(user.password, password):


def user_loader(user_name):
    return User.objects(user_name=user_name).first()
