from app.model.modelImport import *

class Planificacion(db.Model):
    __tablename__ ='planificacion'
    cod = db.Column('cod_planificacion', Integer, primary_key = True, index = True)
    fchPlanificacion = db.Column('fch_planificacion', DateTime, default = datetime.datetime.now, index = True)
    comentarioPlanificacion = db.Column('comentario_planificacion', Text, nullable = True)
    codTipoPlanificacion = db.Column('fk_cod_tipo_planificacion',Integer,ForeignKey('tipo_planificacion.cod_tipo_planificacion'),index = True)
    codEstadoPlanificacion = db.Column('fk_cod_estado_planificacion',Integer,ForeignKey('estado_planificacion.cod_estado_planificacion'),index = True)
    codFinca = db.Column('fk_cod_finca',Integer,ForeignKey('finca.cod_finca'),index = True)
    codGrupoPlanificacion = db.Column('fk_cod_grupo_planificacion',Integer,ForeignKey('grupo_planificacion.cod_grupo_planificacion'),index = True)
    codUsuario = db.Column('fk_cod_usuario', Integer, ForeignKey('usuario.cod_usuario_private'), nullable=False)

    #Relationships
    tipoPlanificacion = relationship('TipoPlanificacion',uselist = False)
    estadoPlanificacion = relationship('EstadoPlanificacion', uselist = False)
    grupoCuadroList = relationship('GrupoCuadro', uselist = True)
    usuario = relationship('Usuario', uselist = False)
    grupoPlanificacion = relationship('GrupoPlanificacion', backref = 'planificacionList')
