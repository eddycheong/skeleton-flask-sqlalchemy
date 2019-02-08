from flask import Flask

app = Flask("__name__")
#app.config['APPLICATION_ROOT'] = '/api'

from .user import *