from flask.ext.admin.contrib.mongoengine import ModelView
from flask.ext.admin.model.template import macro
from flask.ext.login import current_user

from wtforms import fields, widgets


class CKTextAreaWidget(widgets.TextArea):
    def __call__(self, field, **kwargs):
        kwargs.setdefault('class_', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)


class CKTextAreaField(fields.TextAreaField):
    widget = CKTextAreaWidget()


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
    # column_formatters = dict(url=macro('render_price'))
    pass


class NewsView(BaseModelView):
    form_overrides = dict(content=CKTextAreaField, content_ru=CKTextAreaField)
    create_template = 'create.html'
    edit_template = 'edit.html'


class PageAdminView(BaseModelView):
    form_overrides = dict(text=CKTextAreaField)
    list_template = 'admin_page.html'
