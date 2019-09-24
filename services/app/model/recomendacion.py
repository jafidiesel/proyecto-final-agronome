from app.model.modelImport import *

class Recomendacion(db.Model):
    __tablename__ = 'recomendacion'
    cod = db.Column('cod_recomendacion',Integer,primary_key = True,index = True)
    nombre = db.Column('nombre_recomendacion', String(80), nullable = False, unique = True)
    isActiv = db.Column('is_activ', Boolean, nullable = False)

    nombreNomenclador = "recomendacion"


    def __init__(self, nombre, isActiv):
        self.nombre = nombre
        self.isActiv = isActiv

    @staticmethod
    def from_json(json):
        recomendacion = Recomendacion(
            nombre=json.get('nombre'),
            isActiv=json.get('isActiv')
            )
        return recomendacion

    def to_json(self):
        return {
            'id': self.cod,
            'tipoNomenclador': self.nombreNomenclador,
            'nombre': self.nombre,
            'isActiv': self.isActiv
        }