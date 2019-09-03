import os
from datetime import timedelta
from dotenv import load_dotenv

#ruta base del proyecto
BASEDIR = os.path.dirname(os.path.abspath(__file__))


#rutas de enviroment
ENV_VARS = os.path.join(BASEDIR, ".env")

#carga de las variables
load_dotenv(ENV_VARS)


class Config:
    PROJECT_NAME =os.environ.get('PROJECT_NAME')
    CURRENT_DIR =os.path.dirname(os.path.abspath(__file__))
    DB_SERVICE = os.environ.get('DB_SERVICE')
    DB_NAME = os.environ.get('DB_NAME')
    DB_USER = os.environ.get('DB_USER')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    DB_HOST = os.environ.get('DB_HOST')
    DB_PORT = os.environ.get('DB_PORT')
    
    #config de postgrest
    #'postgresql://postgres:postgres@localhost/tutorial'
    DB_URI = '{service}://{user}:{password}@{host}/{db}'.format(
        service = DB_SERVICE,
        user = DB_USER,
        password = DB_PASSWORD,
        host= DB_HOST,
        db= DB_NAME 
    )
    
   

    LOG_IN_DB = {
    'OPTIONS': [],
    'GET': [],
    'POST': [201, 200, 400],
    'PUT': [201, 400],
    'DELETE': [204, 400]
    }

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SLOW_QUERY_TIMEOUT= 0.5
    SQLALCHEMY_RECORD_QUERIES = False

    WTF_CSRF_ENABLED = False

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False

    SQLALCHEMY_DATABASE_URI = Config.DB_URI
    #SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/tutorial'
    MAIL_FLUSH_INTERVAL = 60 #1MINUTO

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}