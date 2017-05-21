from flask import Flask
from werkzeug.utils import import_string
from flask_mongoengine import MongoEngine
from config import config
from config import basedir
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from api.threat import *

db = SQLAlchemy()
mongodb = MongoEngine()

blueprints = [
    {"bp": "api.threat:threat", "url_prefix": "/threat/feed"},
]

def create_app():

    app = Flask(__name__)
    app.config.from_object(config['testing'])
    mongodb.init_app(app)
    db.init_app(app)


    for bp_name in blueprints:
        bp = import_string(bp_name["bp"])
        app.register_blueprint(bp, url_prefix=bp_name["url_prefix"])


    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,password')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
        return response
    return app
