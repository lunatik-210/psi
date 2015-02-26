from . import admin

from flask.ext.admin.contrib.mongoengine import ModelView

from views import ImportantDateView, VideoView

from app.models.models import ImportantDate, Video


admin.add_view(ImportantDateView(ImportantDate, "ImportantDate", endpoint="important_date"))
admin.add_view(VideoView(Video, "Video", endpoint="video"))
