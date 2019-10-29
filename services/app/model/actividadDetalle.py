from app.model.modelImport import *
import datetime

class ActividadDetalle(db.Model):
    __tablename__ = 'actividad_detalle'
    codActivDetalle = db.Column('cod_activ_detalle',Integer,primary_key = True,index = True)
    fchActivDetalle =   db.Column('fch_activ_detalle', DateTime, default=datetime.datetime.now, index = True)
    observacion = db.Column('observacion', String(1024), nullable = True)
    isEliminado = db.Column('is_eliminado', Boolean, default = False, nullable = False)
    
    codActividad = db.Column('fk_cod_actividad',Integer,ForeignKey('actividad.cod_actividad'), nullable = False) #relación
 
    codRecomDetalle = db.Column('fk_cod_recom_detalle',Integer,ForeignKey('recomendacion_detalle.cod_recom_detalle'), nullable = True, index = True)
    codUsuario = db.Column('fk_cod_usuario', Integer, ForeignKey('usuario.cod_usuario_private'), nullable = False)

    actividad = relationship("Actividad", backref="activDetalleList") # N -> 1  &&  1->N (activiDetalleList)

    imgList = relationship('ImgActivDetalle') # 1->N

    paramList = relationship("ActivDetalleParam", backref = "activDetalle")   # 1 -> N 

    usuario = relationship('Usuario', backref = "activDetalleUsuario") # N->1