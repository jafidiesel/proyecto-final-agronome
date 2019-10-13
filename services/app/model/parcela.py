from app.model.modelImport import *

class Parcela(db.Model):
    __tablename__ = 'parcela'
    codParcela = db.Column('cod_parcela',Integer,primary_key = True,index = True)
    nombrePacela =   db.Column('nombre_parcela', String(256), nullable = False)
    superficieParcela =  db.Column('superficie_parcela', Float, nullable = False)
    filas = db.Column('filas',Integer, nullable = False)
    columnas = db.Column('columnas',Integer, nullable = False)

    codFinca = db.Column('fk_cod_finca',Integer,ForeignKey('finca.cod_finca'), nullable = False) #relación

    cuadroList = relationship("Cuadro", backref = "parcela") #1->N