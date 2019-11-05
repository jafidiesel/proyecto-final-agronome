from app.model.modelImport import *

class AnalisisParam(db.Model):
    __tablename__ ='analisis_param'

    codAnalisis = db.Column('fk_cod_analisis', Integer, ForeignKey('analisis.cod_analisis'), primary_key = True)
    codParametro = db.Column('fk_cod_parametro', Integer, ForeignKey('parametro.cod_parametro'), primary_key = True)
    valor = db.Column('valor',String)

    param = relationship('Parametro')