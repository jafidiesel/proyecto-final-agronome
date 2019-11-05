from app.model.modelImport import *
class Parametro(db.Model):
    __tablename__ = 'parametro'
    cod = db.Column('cod_parametro',Integer,primary_key = True,index = True)
    nombre = db.Column('nombre_parametro', String(80), nullable = False,index = True)
    isActiv = db.Column('is_activ', Boolean, nullable = False)
    codTipoParametro = db.Column('fk_cod_tipo_parametro',Integer,ForeignKey('tipo_parametro.cod_tipo_parametro'),index = True)
    codTipoDato = db.Column('fk_cod_tipo_dato',Integer,ForeignKey('tipo_dato.cod_tipo_dato'),index = True)

    def __init__(self, nombre, isActiv):
        self.nombre = nombre
        self.isActiv = isActiv
    

    #Navegabilidad hacia ParametroOpcion 
    paramOpcion = relationship("ParametroOpcion", uselist=True)

    @staticmethod
    def from_json(json):
        parametro = Parametro(
            nombre=json.get('nombre'),
            isActiv=json.get('isActiv')
            )

        return parametro

    def to_json(self):
        return {
            'cod': self.cod,
            'nombre': self.nombre,
            'isActiv': self.isActiv
        }

    def getObjetc(self):
        return self
