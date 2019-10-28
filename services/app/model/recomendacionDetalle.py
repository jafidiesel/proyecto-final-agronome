from app.model.modelImport import *
import datetime

class RecomendacionDetalle(db.Model):
    __tablename__ = 'recomendacion_detalle'
    codRecomDetalle = db.Column('cod_recom_detalle',Integer,primary_key = True,index = True)
    fchRecomDetalle =   db.Column('fch_recom_detalle', DateTime, default=datetime.datetime.now, index = True)
    observacion = db.Column('observacion', String(1024), nullable = True)
    isEliminado = db.Column('is_eliminado', Boolean, default = False, nullable = False)
    isAplicada = db.Column('is_aplicada', Boolean, default = False, nullable = True)

    codRecomendacion = db.Column('fk_cod_recomendacion',Integer,ForeignKey('recomendacion.cod_recomendacion'), nullable = False) #relación

    codUsuario=  db.Column('fk_cod_usuario',Integer,ForeignKey('usuario.cod_usuario_private'), nullable = False)


    recomendacion = relationship("Recomendacion", backref="recomDetalleList") # N -> 1  &&  1->N 
    activDetalle = relationship("ActividadDetalle", backref = "recomendacionDetalle") # 1->1 fk en actividad
    paramList = relationship("RecomDetalleParam", backref = "recomDetalle")   # 1 -> N
    
    usuario = relationship("Usuario", backref = "recomDetalleUsuario") # N -> 1

    analisisList = relationship("Analisis") #1 -> N