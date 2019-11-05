from app.model.modelImport import *

class CuadroCultivo(db.Model):
    __tablename__ ='cuadro_cultivo'
    cod = db.Column('cod_cuadro_cultivo', Integer, primary_key = True, index = True)
    fchIni = db.Column('fch_ini', DateTime, default = datetime.datetime.now, index = True)
    fchFin = db.Column('fch_fin', DateTime, index = True)
    codGrupoCuadro = db.Column('fk_cod_grupo_cuadro',Integer,ForeignKey('grupo_cuadro.cod_grupo_cuadro'),index = True)
    codCultivo = db.Column('fk_cod_cultivo',Integer,ForeignKey('cultivo.cod_cultivo'),index = True)
    codCuadro = db.Column('fk_cod_cuadro',Integer,ForeignKey('cuadro.cod_cuadro'),index = True)
    #Relationships
    cultivo = relationship('Cultivo', uselist = False)
    cuadro = relationship('Cuadro', uselist = False)
