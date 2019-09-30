from app.model.modelImport import *

class Actividad(db.Model):
    __tablename__ = 'actividad'
    cod = db.Column('cod_actividad',Integer,primary_key = True,index = True)
    nombre = db.Column('nombre_actividad', String(80), nullable = False, unique = True)
    isActiv = db.Column('is_activ', Boolean, nullable = False)
    nombreNomenclador = "actividad"


    def __init__(self, nombre, isActiv):
        self.nombre = nombre
        self.isActiv = isActiv

    @staticmethod
    def from_json(json):
        actividad = Actividad(
            nombre=json.get('nombre'),
            isActiv=json.get('isActiv')
            )
        return actividad

    def to_json(self):
        return {
            'cod': self.cod,
            'tipoNomenclador': self.nombreNomenclador,
            'nombre': self.nombre,
            'isActiv': self.isActiv
        }