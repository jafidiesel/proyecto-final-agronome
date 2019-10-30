from app.model.modelImport import *

class GrupoCuadro(db.Model):
    __tablename__ ='grupo_cuadro'
    cod = db.Column('cod_grupo_cuadro', Integer, primary_key = True, index = True)
    codParcela = db.Column('fk_cod_parcela',Integer,ForeignKey('parcela.cod_parcela'),index = True)
    codPlanificacion = db.Column('fk_cod_planificacion',Integer,ForeignKey('planificacion.cod_planificacion'),index = True)
    #Relationships
    parcela = relationship('Parcela', uselist = False)
    cuadroCultivoList = relationship('CuadroCultivo',uselist= True)
    analisisList = relationship('Analisis',uselist = True)
    planList = relationship('Plan',uselist = True)

