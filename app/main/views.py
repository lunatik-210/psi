import datetime

from flask import render_template, request, make_response, send_file, abort

from app.models.models import ImportantDate, NewsItem, Video, Image
from app import constants
from io import BytesIO

def main():
    locale = request.cookies.get(constants.LOCALE_TOKEN)
    template = render_template('main.html',
                               dates=ImportantDate.objects.all(),
                               news=NewsItem.objects.all(),
                               locale=locale)
    resp = make_response(template)

    if not locale:
        resp.set_cookie(constants.LOCALE_TOKEN, constants.DEFAULT_LOCALE,
                        expires=datetime.datetime.now() + datetime.timedelta(days=constants.COOKIE_LIFETIME_DAYS))
    return resp


def video():
    locale = request.cookies.get(constants.LOCALE_TOKEN)
    return render_template('video.html',
                           dates=ImportantDate.objects.all(),
                           news=NewsItem.objects.all(),
                           videos=Video.objects.all(),
                           locale=locale)

def pictures():
    return render_template('pictures.html',
                            images=Image.objects.all(),
                            dates=ImportantDate.objects.all(),
                            news=NewsItem.objects.all())

def images(filename=None):
  if filename:
    for image in Image.objects():
      if filename == image.image.name:
        return send_file(BytesIO(image.image.read()), mimetype='image')
  abort(404)
