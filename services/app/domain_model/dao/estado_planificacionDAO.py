
#https://docs.sqlalchemy.org/en/13/orm/extensions/associationproxy.html?highlight=data%20access%20object
from flask_sqlalchemy import SQLAlchemy
from app.app import db

class EstadoPlanificacionDAO:
    
    #constructor    
    def __init__(self, db):
        self.db = db
   

    def insertValues(self, EstadoPlanificacion):
       
    def selectAll(self):
        return EstadoPlanificacion.query.all()
    
    def selectOne(self)::   
   
    def update(self):
       
    #def dropTable(self):
        