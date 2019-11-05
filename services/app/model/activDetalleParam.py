from app.model.modelImport import *
class ActivDetalleParam(db.Model):
    __tablename__ = 'activ_detalle_param'
    codActivDetalle = db.Column('fk_cod_activ_detalle',Integer,ForeignKey('actividad_detalle.cod_activ_detalle'),primary_key = True)
    codParametro =  db.Column('fk_cod_parametro',Integer,ForeignKey('parametro.cod_parametro'), primary_key = True)
    valor = db.Column('valor', String) 
    param = relationship("Parametro") #N->1