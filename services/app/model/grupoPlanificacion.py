from app.model.modelImport import *

class GrupoPlanificacion(db.Model):
    __tablename__ ='grupo_planificacion'
    cod = db.Column('cod_grupo_planificacion', Integer, primary_key = True, index = True)
    fchCreacion = db.Column('fch_creacion', DateTime, default = datetime.datetime.now, index = True)
    nombreGrupoPlanificacion = db.Column('comentario_planificacion', String(120), nullable = False, unique = True)
    isActiv =  db.Column('is_activ', Boolean, nullable = False)
    codFinca = db.Column('fk_cod_finca',Integer,ForeignKey('finca.cod_finca'),index = True)
    #Relationships
    planificaciones = relationship('Planificacion',uselist = True)
