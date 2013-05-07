import os, sys, inspect
sys.path.append(os.path.join(os.path.abspath('.'), 'lib'))

from google.appengine.ext.webapp.util import run_wsgi_app
from src import app

run_wsgi_app(app)