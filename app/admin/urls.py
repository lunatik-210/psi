from . import admin

from flask.ext.admin.contrib.mongoengine import ModelView

from views import ImportantDateView, PageAdminView

from app.models import ImportantDate, Page


admin.add_view(PageAdminView(Page, "Page", endpoint="page"))
admin.add_view(ImportantDateView(ImportantDate, "ImportantDate", endpoint="important_date"))
