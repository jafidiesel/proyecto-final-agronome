from flask import Flask
from app.settings import DevConfig
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_object=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:testing@localhost:5432/agronome'
    db.init_app(app)

    return app