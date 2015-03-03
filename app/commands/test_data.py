 # -*- coding: utf-8 -*-

from . import test_data
from app.models.models import User, Video, NewsItem, ImportantDate

@test_data.command
def create():
    "Fill database with test data"
    user = User(user_name="admin", password="admin")
    user.save()

    videos = [('qbWUXNPf65A', 'NAME1'), ('cBsMCDgd3lg', 'NAME2'),
              ('KoyA0PStmls', 'NAME3'), ('AjfejT2DrJo', 'NAME4'), ('0WQTgIC1Pfs', 'NAME5'), ('0WQTgIC1Pfs', 'NAME6')]

    for url,name in videos:
        video = Video(url=url, name=name)
        video.save()

    news = [["The PSI'14 is open. Congratulations to the Conference participants and organizers! See some photographs taken at the opening.",
    u"Поздарвляем всех участников и организаторов! Несколько фоток уже выложено!"],
    ["The Programme of Workshop on Science Intensive Applied Software is available in PDF (in Russian).",
    u"Программа конференции уже доступна на русском языке"],
    ["The Programme of Workshop 'Educational Informatics' is available in PDF.",
    u"Программа конференции уже доступна в PDF"],
    ["Registration for the conference begins at 8.00 am June 24 at New Peterhof Hotel.",
    u"Регестрация на конференцию начинается в 8.00 24 июня"]]

    for n in news:
        newsItem = NewsItem(content=n[0], content_ru=n[1])
        newsItem.save()

    dates = [["abstract submission", u"прием докладов"], ["submission deadline", u"прием докладов закончен"], ["notification of acceptance",
    u"рассылка приглашений"], ["camera ready papers for pre-proceedings", u"что-то там готово для обработки"], 
    ["the conference dates", u"план конференции"], ["camera ready papers due", u"что то там заканчивается"]]

    for d in dates:
        date = ImportantDate(description=d[0], description_ru=d[1])
        date.save()



@test_data.command
def delete():
    "Delete all data from database"
    User.drop_collection()
    Video.drop_collection()
    NewsItem.drop_collection()
    ImportantDate.drop_collection()


@test_data.command
def recreate():
    "Delete all data from database and then fill it again"
    delete()
    create()
