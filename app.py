#!flask/bin/python
from app import create_app
from flask.ext.script import Manager

from app.commands import test_data

manager = Manager(create_app)
manager.add_option('-c', '--config', dest='config', required=False)
manager.add_command('test_data', test_data)

if __name__ == '__main__':
    manager.run()
