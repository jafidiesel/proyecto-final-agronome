from app.model.modelImport import *

class TipoDato(db.Model):
    __tablename__ = 'tipo_dato'
    cod = db.Column('cod_tipo_dato',Integer,primary_key = True,index = True)
    nombre= db.Column('nombre_tipo_dato', String(80), nullable = False, unique = True)
    isActiv = db.Column('is_activ', Boolean, nullable = False)
    nombreNomenclador = "tipoDato"
    #parametroDatoRef = relationship("Parametro", back_populates="datoParametroRef", uselist=True)
    parametroDato = relationship("Parametro", backref="tipoDatoRef", uselist=True)

    def __init__(self, nombre, isActiv):
        self.nombre = nombre
        self.isActiv = isActiv

    @staticmethod
    def from_json(json):
        tipoDato = TipoDato(
            nombre=json.get('nombre'),
            isActiv=json.get('isActiv')
            )
        return tipoDato

    def to_json(self):
        return {
            'cod': self.cod,
            'tipoNomenclador': self.nombreNomenclador,
            'nombre': self.nombre,
            'isActiv': self.isActiv
        }