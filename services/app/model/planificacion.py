from app.model.modelImport import *

class Planificacion(db.Model):
    __tablename__ ='planificacion'
    codPlanificacion = db.Column('cod_planificacion', Integer, primary_key = True, index = True)
    fchPlanificacion = db.Column('fch_planificacion', DateTime, default = datetime.datetime.now, index = True)
    comentarioPlanifiacion = db.Column('comentario_planificacion', Text, nullable = True)
    codTipoPlanificacion = db.Column('fk_cod_tipo_planificacion',Integer,ForeignKey('tipo_planificacion.cod_tipo_planificacion'),index = True)
    #Relationships
    tipoPlanificacion = relationship('TipoPlanificacion',uselist = False)