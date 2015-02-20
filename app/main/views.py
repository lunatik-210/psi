from flask import render_template

from app.models.models import ImportantDate, NewsItem


def hello_world():
    return render_template('main.html', dates=ImportantDate.objects.all(),
                           news=NewsItem.objects.all())
