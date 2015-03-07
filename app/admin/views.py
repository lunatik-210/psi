from flask.ext.admin.contrib.mongoengine import ModelView
from flask.ext.login import current_user

from wtforms import fields, widgets
from flask.ext.admin import BaseView, expose
from app.models import  Page
from flask.ext import wtf

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
    form_overrides = dict(description=CKTextAreaField)
    create_template = 'create.html'
    edit_template = 'edit.html'


class VideoView(BaseModelView):
    pass


class NewsView(BaseModelView):
    form_overrides = dict(content=CKTextAreaField)
    create_template = 'create.html'
    edit_template = 'edit.html'


class PageAdminView(BaseModelView):
    form_overrides = dict(text=CKTextAreaField)
    #list_template = 'admin_page.html'
    create_template = 'createPage.html'
    edit_template = 'edit.html'

    @expose('/')
    def index(self):
        return self.render('admin_page.html', data=Page.objects.all())


    @expose('/act/')
    def action_view(self):
        pass
