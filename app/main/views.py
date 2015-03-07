import datetime

from flask import render_template, request, make_response

from app.models.models import ImportantDate, NewsItem, Video
from app import constants
from app.models import  Page

def main():
    locale = request.cookies.get(constants.LOCALE_TOKEN)
    template = render_template('main.html',
                               dates=ImportantDate.objects.all(),
                               news=NewsItem.objects.all())
    resp = make_response(template)

    if not locale:
        resp.set_cookie(constants.LOCALE_TOKEN, constants.DEFAULT_LOCALE,
                        expires=datetime.datetime.now() + datetime.timedelta(days=constants.COOKIE_LIFETIME_DAYS))
    return resp


def video():
    return render_template('video.html',
                           dates=ImportantDate.objects.all(),
                           news=NewsItem.objects.all(),
                           videos=Video.objects.all())
