from collections import deque
from urlparse import urlparse, parse_qs
from io import BytesIO

from flask import render_template, request, send_file, abort, redirect, url_for

from app.models.models import ImportantDate, NewsItem, Video, Image, Speaker, Page, MainPage
from app import constants


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


class Node():
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, node):
        self.children.append(node)


def reconstruct(pages):
    queue = deque(pages)
    d = dict()
    d['None'] = Node('None')
    while not len(queue) == 0:
        node = queue.popleft()
        new_node = Node(node)
        if str(node.parent) in d:
            d[node.parent].add_child(new_node)
        else:
            queue.append(node)
        d[str(node.pk)] = new_node
    return d['None'].children


def get_page_data():
    locale = request.cookies.get(constants.LOCALE_TOKEN) or constants.DEFAULT_LOCALE
    data = reconstruct(Page.objects.all())
    return dict(dates=ImportantDate.objects.all(),
                news=NewsItem.objects.all(),
                locale=locale,
                video_tags=get_tags(Video),
                data=data,
                picture_tags=get_tags(Image))


def main():
    page = MainPage.objects.first()

    return render_template('main.html', page=page, speakers=Speaker.objects.all(), **get_page_data())


def video():
    tag = request.args.get('tag', None)
    videos = Video.objects.all()
    if tag:
        videos = Video.objects.filter(tag=tag).all()

    for video in videos:
        video.video_id = parse_qs(urlparse(video.url).query)['v'][0]

    return render_template('video.html',
                           videos=videos, **get_page_data())


def pictures():
    tag = request.args.get('tag', None)
    images = Image.objects.all()
    if tag:
        images = Image.objects.filter(tag=tag).all()
    return render_template('pictures.html',
                           images=images, **get_page_data())


def speakers():
    return render_template('speakers.html',
                           speakers=Speaker.objects.all(), **get_page_data())


def menu():
    title = request.args.get('title', None)

    if title is None:
        return redirect(url_for('main.main'))

    try:
        page = Page.objects.filter(title=title).first()
    except AttributeError:
        return redirect(url_for('main.main'))

    return render_template('menu_content.html',
                           page=page, **get_page_data())


def images(filename=None):
    if filename:
        for image in Image.objects():
            if filename == image.image.name:
                return send_file(BytesIO(image.image.read()), mimetype='image')
        for spekaer in Speaker.objects():
            if filename == spekaer.photo.name:
                return send_file(BytesIO(spekaer.photo.read()), mimetype='image')
    abort(404)
