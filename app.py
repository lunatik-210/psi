#!flask/bin/python
from app import create_app
from flask.ext.script import Manager

manager = Manager(create_app)
manager.add_option('-c', '--config', dest='config', required=False)

if __name__ == '__main__':
    manager.run()
