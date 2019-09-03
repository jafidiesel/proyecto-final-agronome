from flask import Flask
from flask_cors import CORS
from app.extensions import api,db,migrate
from app.api.helperApi.hlNamespaceBackend import NAMESPACES
from config import config 

def create_api(environment_name=None):
    app= Flask(__name__)

    app.config.from_object(config[environment_name])

    CORS(app)

    for namespace in NAMESPACES:
        api.add_namespace(namespace)

    with app.app_context():
        db.init_app(app)
        migrate.init_app(app, db)

    api.init_app(app)
    return app

