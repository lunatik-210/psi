from flask import request
from flask import Response

from important_dates import *

from app import db


def add_important_date():
    """ accepts json document from request data """
    # TODO this DAO is bullshit. rewrite
    dao = ImportantDatesDAO(db.db)
    dao.save(request.get_json())
    return Response(status=200)


def fetch_all_dates():
    dao = ImportantDatesDAO(db.db)
    return Response(dao.find_all(), mimetype="application/json")


def fetch_dates_range():
    dao = ImportantDatesDAO(db.db)
    skip = request.args.get('skip', 0)
    limit = request.args.get('limit', 0)
    return Response(dao.find_range(skip, limit), mimetype="application/json")
