from . import admin

from views import ImportantDateView, VideoView, PageAdminView, NewsView, BaseModelView, SpeakersView

from app.models import ImportantDate, Page, Video, NewsItem, Image, Speaker


admin.add_view(PageAdminView(Page, "Page", endpoint="page"))
admin.add_view(ImportantDateView(ImportantDate, "ImportantDate", endpoint="important_date"))
admin.add_view(NewsView(NewsItem, "News", endpoint="news"))
admin.add_view(VideoView(Video, "Video", endpoint="video"))
admin.add_view(BaseModelView(Image, "Image", endpoint="image"))
admin.add_view(SpeakersView(Speaker, "Speaker", endpoint="speaker"))
