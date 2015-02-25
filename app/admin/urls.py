from . import admin

from flask.ext.admin.contrib.mongoengine import ModelView

from views import ImportantDateView

from app.models.models import ImportantDate


admin.add_view(ImportantDateView(ImportantDate, "ImportantDate", endpoint="important_date"))
