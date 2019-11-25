from app.model.modelImport import *
import datetime

class LibroCampo(db.Model):
    __tablename__ = 'libro_campo'
    codLibroCampo = db.Column('cod_libro_campo', Integer, primary_key = True, index = True)
    nombreLibroCampo = db.Column('nombre_libro_campo', String(80), nullable = False, index = True)
    fchIni = db.Column('fch_ini', DateTime, default = datetime.datetime.now, nullable = False, index = True)
    fchFin = db.Column('fch_fin', DateTime, nullable = True, index = True)

    #relaciones de tablas
    codFinca = db.Column('fk_cod_finca',Integer,ForeignKey('finca.cod_finca'), nullable = False) 
    codGrupoPlanificacion = db.Column('fk_cod_grupo_planificacion',Integer,ForeignKey('grupo_planificacion.cod_grupo_planificacion'), nullable = False)
    codCultivo = db.Column('fk_cod_cultivo',Integer,ForeignKey('cultivo.cod_cultivo'), nullable = False)


    #relationship
    grupoPlanificacion = relationship("GrupoPlanificacion") #1->1 
    activDetalleList = relationship("ActividadDetalle",backref = "libroCampoActivDetalle")  #1 -> N
    recomDetalleList = relationship("RecomendacionDetalle",backref = "libroCampoRecomDetalle")  #1 -> N
   