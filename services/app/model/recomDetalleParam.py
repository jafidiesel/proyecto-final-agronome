from app.model.modelImport import *
class RecomDetalleParam(db.Model):
    __tablename__ = 'recom_detalle_param'
    codRecomDetalle = db.Column('fk_cod_recom_detalle',Integer,ForeignKey('recomendacion_detalle.cod_recom_detalle'),primary_key = True)
    codParametro =  db.Column('fk_cod_parametro',Integer,ForeignKey('parametro.cod_parametro'), primary_key = True)
    valor = db.Column('valor', String) 
    param = relationship("Parametro") #N->1