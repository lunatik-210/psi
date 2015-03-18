#!flask/bin/python
from flask.ext.script import Manager
from mongoengine.queryset import manager

from app import create_app
from app.Gunicorn import GunicornServer
from app.commands import test_data


manager = Manager(create_app)
# manager.add_option('-c', '--config', dest='config', required=False)
manager.add_command('test_data', test_data)
manager.add_command('gunicorn', GunicornServer())

if __name__ == '__main__':
    manager.run()
