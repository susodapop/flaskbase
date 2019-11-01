'''
This module provides a base for developing self-container Flask blueprints. It
makes no assumptions about your environment. To add a blueprint, add a call to
`register_blueprints` in the blueprints directory.

If the blueprints directory does not exist on first run, this file will build it.
'''

import flask, os


bp_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "blueprints")

if not os.path.exists(bp_dir):
    os.makedirs(bp_dir)
    with open(os.path.join(bp_dir, '__init__.py'), 'w') as fp:
    	base_code = '''def register_blueprints(app):\n\treturn app'''	
    	fp.write(base_code)


app = flask.Flask(__name__)

from blueprints import register_blueprints

register_blueprints(app)
