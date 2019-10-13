from app.model.modelImport import *

class Finca(db.Model):
    __tablename__ = 'finca'
    codFinca = db.Column('cod_finca',Integer,primary_key = True,index = True)
    nombreFinca =   db.Column('nombre_finca', String(256), nullable = False)
    superficie = db.Column('superficie', Float, nullable = False)
    isActiv = db.Column('is_activ', Boolean, nullable = False)

    calle =  db.Column('calle_finca', String(256), nullable = True)
    nro= db.Column('nro_finca', Integer, nullable = True)
    localidad = db.Column('localidad_finca', String(50), nullable = True)
    provincia = db.Column('provincia_finca', String(50), nullable = True)
    urlMaps= db.Column('urlmaps_finca', String(512), nullable = True)

    parcelaList = relationship("Parcela", backref = "fincaParcela") #1->N