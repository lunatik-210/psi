from . import admin

from flask.ext.admin.contrib.mongoengine import ModelView

from app.models.models import ImportantDate


admin.add_view(ModelView(ImportantDate))

#admin.add_view(TariffView(Tariffs, "Tariffs", endpoint="tariffs"))

#admin.add_view(ExportView(name='csv', endpoint="export/csv", category='Export'))

#admin.add_view(ExportView(name='json', endpoint="export/json", category='Export'))
