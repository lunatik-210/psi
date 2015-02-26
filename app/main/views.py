from flask import render_template

from app.models.models import ImportantDate, NewsItem, Video


def main():
    return render_template('main.html', 
                            dates=ImportantDate.objects.all(),
                            news=NewsItem.objects.all())

def video():
    return render_template('video.html', 
                            dates=ImportantDate.objects.all(),
                            news=NewsItem.objects.all(),
                            videos=Video.objects.all())
