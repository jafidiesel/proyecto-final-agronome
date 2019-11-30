from app.model.modelImport import *

class Cultivo(db.Model):
    __tablename__ ='cultivo'
    cod = db.Column('cod_cultivo', Integer, primary_key = True, index = True)
    cantidadCultivo = db.Column('cantidad_cultivo', Integer,nullable = False)
    produccionEsperada = db.Column('produccion_esperada', Float, nullable = False)
    variedadCultivo = db.Column('variedad_cultivo', String(120), nullable = False)
    cicloUnico = db.Column('ciclo_unico', Boolean, nullable = False)
    tipoCultivo = db.Column('fk_cod_tipo_cultivo',Integer,ForeignKey('tipo_cultivo.cod_tipo_cultivo'),index = True)

    tipoCultivoR = relationship("TipoCultivo", uselist = False) #1->N

    