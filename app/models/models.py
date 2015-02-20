from app import db
import datetime


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
    path = db.StringField()
    folder = db.StringField()
    meta = {'collection': 'videos'}
