from app import db

from flask.ext.login import UserMixin

import datetime


class Page(db.Document):
    title = db.StringField(max_length=256)
    text = db.StringField()
    parent = db.StringField(max_length=256)
    meta = {'collection': 'pages'}

class ImportantDate(db.Document):
    date = db.DateTimeField(default=datetime.datetime.now)
    description = db.StringField(max_length=256)
    meta = {'collection': 'important_dates'}


class NewsItem(db.Document):
    date = db.DateTimeField(default=datetime.datetime.now)
    content = db.StringField()
    meta = {'collection': 'news'}


class Speaker(db.Document):
    first_name = db.StringField(max_length=64)
    last_name = db.StringField(max_length=64)
    university = db.StringField(max_length=256)
    bio_reference_link = db.StringField(max_length=256)
    description = db.StringField()
    path_to_photo = db.StringField(max_length=128)
    meta = {'collection': 'speakers'}


class Image(db.Document):
    description = db.StringField()
    image = db.ImageField()
    folder = db.StringField()
    meta = {'collection': 'image'}


class Video(db.Document):
    path = db.StringField(max_length=256)
    folder = db.StringField(max_length=256)
    meta = {'collection': 'videos'}


class MenuItem(db.Document):
    id = db.StringField()
    title = db.StringField()
    link = db.StringField()
    childsId = db.ListField(db.StringField())
    meta = {'collection': 'menu'}


class User(db.Document, UserMixin):
    """An admin user capable of viewing reports.

    :param str email: email address of user
    :param str password: encrypted password for the user

    """
    user_name = db.StringField()
    password =db.StringField()
    meta = {'collection': 'users'}

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.user_name
