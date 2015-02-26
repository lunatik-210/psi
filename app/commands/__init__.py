from flask.ext.script import Manager

test_data = Manager(usage="Perform test database operations")

from test_data import * 