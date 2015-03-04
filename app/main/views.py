import datetime

from flask import render_template, request, make_response, send_file, abort

from app.models.models import ImportantDate, NewsItem, Video, Image
from app import constants
from io import BytesIO


def get_tags(model):
    filter = []
    tags = []
    for object in model.objects():
        if object.tag and object.tag not in filter:
            filter.append(object.tag)
            tags.append(dict(en=object.tag, ru=object.tag_ru))
    if len(filter) == 0:
        return None
    return tags    


def get_picture_tags():
    return get_tags(Image)


def get_video_tags():
    return get_tags(Video)


def main():
    locale = request.cookies.get(constants.LOCALE_TOKEN)
    return render_template('main.html',
        dates=ImportantDate.objects.all(),
        news=NewsItem.objects.all(),
        locale=locale,
        video_tags=get_video_tags(),
        picture_tags=get_picture_tags())


def video():
    tag = request.args.get('tag', None)
    videos = Video.objects.all()
    if tag:
        videos = Video.objects.filter(tag=tag).all()

    locale = request.cookies.get(constants.LOCALE_TOKEN)
    return render_template('video.html',
        dates=ImportantDate.objects.all(),
        news=NewsItem.objects.all(),
        video_tags=get_video_tags(),
        picture_tags=get_picture_tags(),
        videos=videos)

def pictures():
    tag = request.args.get('tag', None)
    images = Image.objects.all()
    if tag:
        images = Image.objects.filter(tag=tag).all()

    locale = request.cookies.get(constants.LOCALE_TOKEN)
    return render_template('pictures.html',
        dates=ImportantDate.objects.all(),
        news=NewsItem.objects.all(),
        locale=locale,
        video_tags=get_video_tags(),
        picture_tags=get_picture_tags(),
        images=images)


def images(filename=None):
    if filename:
        for image in Image.objects():
            if filename == image.image.name:
                return send_file(BytesIO(image.image.read()), mimetype='image')
    abort(404)
