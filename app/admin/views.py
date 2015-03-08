from flask import url_for, redirect, request, render_template, session
from flask.ext import wtf
from flask.ext.admin import expose, AdminIndexView, BaseView
from flask.ext.admin.contrib.mongoengine import ModelView
from flask.ext.admin.model.template import macro
from flask.ext.login import current_user, login_user, logout_user
from wtforms import fields, widgets
from app.models import User, Page
from app.admin.auth.singnin_form import SigninForm


LOGGED_IN_TOKEN = 'logged_in'


class CKTextAreaWidget(widgets.TextArea):
    def __call__(self, field, **kwargs):
        kwargs.setdefault('class_', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)


class CKTextAreaField(fields.TextAreaField):
    widget = CKTextAreaWidget()


class PageForm(wtf.Form):
    title = fields.TextField('Title')
    text = CKTextAreaField('Text')
    #parent = fields.SelectField('Parent')
    '''def __init__(self, lst):
        super(PageForm, self)
        self.parent.choices = lst[:]
        self._fields = [self.title,self.text,self.parent]'''


class BaseModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated()


class ImportantDateView(BaseModelView):
    form_overrides = dict(description=CKTextAreaField, description_ru=CKTextAreaField)
    create_template = 'create.html'
    edit_template = 'edit.html'


class SpeakersView(BaseModelView):
    column_list = ('photo', 'name', 'name_ru', 'country', 'country_ru', 'bio_reference_link')

    form_overrides = dict(description=CKTextAreaField, description_ru=CKTextAreaField)
    create_template = 'create.html'
    edit_template = 'edit.html'


class VideoView(BaseModelView):
    list_template = "video/video_list.html"
    create_template = "video/video_create.html"
    column_formatters = dict(url=macro('render_url'))
    pass


class NewsView(BaseModelView):
    form_overrides = dict(content=CKTextAreaField, content_ru=CKTextAreaField)
    create_template = 'create.html'
    edit_template = 'edit.html'


class PageAdminView(BaseModelView):
    form_overrides = dict(text=CKTextAreaField)

    create_template = 'createPage.html'
    edit_template = 'edit.html'

    @expose('/')
    def index(self):
        return self.render('admin_page.html', data=Page.objects.all())


    @expose('/act/')
    def action_view(self):
        pass


class DefaultLoginView(AdminIndexView):
    def __init__(self):
        super(DefaultLoginView, self).__init__(name="Authorization")

    @expose('/')
    def index(self):
        if current_user is not None and current_user.is_authenticated():
            return self.render("logout.html")
        return render_template('login.html', signin_form=SigninForm())

    @expose('/login', methods=('GET', 'POST'))
    def login_view(self):
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

    @expose('/logout')
    def logout_view(self):
        session.pop(LOGGED_IN_TOKEN)
        logout_user()
        return redirect(url_for('.index'))
