from app.models.api import AccessObject


class ImportantDatesDAO(AccessObject):
    def __init__(self, db):
        AccessObject.__init__(self, db, 'important_dates')
