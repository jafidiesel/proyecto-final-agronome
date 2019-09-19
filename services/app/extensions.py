from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Api

api = Api(version='v1.0', title='AgronoMe',description='Servicios del Sistema AgronoMe',default='http://localhost:9001/api/',default_label ='Url principal')

db= SQLAlchemy()

migrate = Migrate()