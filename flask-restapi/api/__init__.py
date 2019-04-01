from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app = Flask(__name__)
app.config.from_object('api.config')

db = SQLAlchemy(app)

from .controller import api_bp
app.register_blueprint(api_bp, url_prefix='/api')

db.init_app(app)