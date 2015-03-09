from collections import deque

from flask import url_for, redirect, request, render_template, session
from flask.ext import wtf
from flask.ext.admin import expose, AdminIndexView
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
    title_ru = fields.TextField('TitleRu')
    text = CKTextAreaField('Text')
    text_ru = CKTextAreaField('TextRu')

    # parent = fields.SelectField('Parent')
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


class NewsView(BaseModelView):
    form_overrides = dict(content=CKTextAreaField, content_ru=CKTextAreaField)
    create_template = 'create.html'
    edit_template = 'edit.html'


class PageAdminView(BaseModelView):
    form_overrides = dict(text=CKTextAreaField, text_ru=CKTextAreaField)
    create_template = 'page/create_page.html'
    edit_template = 'page/page_edit.html'

    class Node():
        def __init__(self, value):
            self.value = value
            self.children = []

        def add_child(self, node):
            self.children.append(node)

    @staticmethod
    def reconstruct(pages):
        queue = deque(pages)
        id_to_node = dict()
        id_to_node['None'] = PageAdminView.Node('None')
        while not len(queue) == 0:
            node = queue.popleft()
            new_node = PageAdminView.Node(node)
            if str(node.parent) in id_to_node:
                id_to_node[node.parent].add_child(new_node)
            else:
                queue.append(node)
            id_to_node[str(node.pk)] = new_node
        return id_to_node['None'].children, id_to_node

    @staticmethod
    def delete_children(node):
        for child in node.children:
            PageAdminView.delete_children(child)
        Page.objects(pk=node.value.id).delete()

    @expose('/')
    def index(self):
        data, id_to_node = self.reconstruct(Page.objects.all())
        return self.render('page/page_list.html', data=data)

    @expose('/remove/')
    def action_view(self):
        data, id_to_node = self.reconstruct(Page.objects.all())
        node = id_to_node[request.args['id']]
        PageAdminView.delete_children(node)
        return redirect(url_for(".index"))


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
