from app.model.modelImport import *

class Cuadro(db.Model):
    __tablename__ = 'cuadro'
    codCuadro = db.Column('cod_cuadro',Integer,primary_key = True,index = True)
    nombreCuadro =   db.Column('nombre_cuadro', String(256), nullable = False)
    codParcela = db.Column('fk_cod_parcela',Integer,ForeignKey('parcela.cod_parcela'), nullable = False) #relación