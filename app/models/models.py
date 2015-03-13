import datetime

from flask.ext.login import UserMixin

from app import db

class MainPage(db.Document):
    text = db.StringField()
    text_ru = db.StringField()
    meta = {'collection': 'main_page'}


class Page(db.Document):
    title = db.StringField(max_length=256)
    title_ru = db.StringField(max_length=256)
    text = db.StringField()
    text_ru = db.StringField()
    parent = db.StringField(max_length=256)
    meta = {'collection': 'pages'}


class ImportantDate(db.Document):
    date = db.DateTimeField(default=datetime.datetime.now)
    description = db.StringField()
    description_ru = db.StringField()
    meta = {'collection': 'important_dates'}


class NewsItem(db.Document):
    date = db.DateTimeField(default=datetime.datetime.now)
    content = db.StringField()
    content_ru = db.StringField()
    meta = {'collection': 'news'}


class Speaker(db.Document):
    photo = db.ImageField()
    name = db.StringField(max_length=256)
    name_ru = db.StringField(max_length=256)
    country = db.StringField(max_length=256)
    country_ru = db.StringField(max_length=256)
    description = db.StringField()
    description_ru = db.StringField()

    bio_reference_link = db.StringField(max_length=256)

    # path_to_photo = db.StringField(max_length=128)
    
    meta = {'collection': 'speakers'}


class Image(db.Document):
    image = db.ImageField()
    tag = db.StringField(max_length=256)
    tag_ru = db.StringField(max_length=256)
    meta = {'collection': 'image'}


class Video(db.Document):
    url = db.StringField(max_length=256)
    name = db.StringField(max_length=256)
    name_ru = db.StringField(max_length=256)
    tag = db.StringField(max_length=256)
    tag_ru = db.StringField(max_length=256)
    meta = {'collection': 'videos'}


class MenuItem(db.Document):
    id = db.StringField()
    title = db.StringField()
    title_ru = db.StringField()
    link = db.StringField()
    childsId = db.ListField(db.StringField())
    meta = {'collection': 'menu'}


class User(db.Document, UserMixin):
    """An admin user capable of viewing reports.

    :param str email: email address of user
    :param str password: encrypted password for the user

    """
    user_name = db.StringField()
    password = db.StringField()
    meta = {'collection': 'users'}

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.user_name

