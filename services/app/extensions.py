from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Api

api = Api(version='v0.1',title='Tutorial Api', description = 'tutorial api rest')

db= SQLAlchemy()

migrate = Migrate()