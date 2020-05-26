from flask import Flask
#from backend.ext import configuration
from backend.ext import appearance
from backend.ext import database
from backend.ext import auth
from backend.ext import admin
from backend.ext import commands

from backend.blueprints import restapi
from backend.blueprints import webui


def create_app():
    app = Flask(__name__)
    #configuration.init_app(app)
    appearance.init_app(app)
    database.init_app(app)
    auth.init_app(app)
    admin.init_app(app)
    commands.init_app(app)
    return app
