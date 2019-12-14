from database import Session
from flask import Flask, Blueprint

session = Session()

api = Blueprint("api", "api", url_prefix="/api")

from .users import *

app = Flask("__name__")
app.register_blueprint(api)
