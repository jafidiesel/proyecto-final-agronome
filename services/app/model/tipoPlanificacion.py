from app.model.modelImport import *

class TipoPlanificacion(db.Model):
    __tablename__ = 'tipo_planificacion'
    cod = db.Column('cod_tipo_planificacion',Integer,primary_key = True,index = True)
    nombre = db.Column('nombre_tipo_planificacion', String(80), nullable = False, unique = True,index = True)
    isActiv = db.Column('is_activ', Boolean, nullable = False)
    nombreNomenclador = "tipoPlanificacion"    

    def __init__(self, nombre,isActiv):
        self.nombre = nombre
        self.isActiv = isActiv

    @staticmethod
    def from_json(json):
        tipoPlanificacion = TipoPlanificacion(
            nombre=json.get('nombre'),            
            isActiv=json.get('isActiv')
            )
        return tipoPlanificacion

    def to_json(self):
        return {
            'cod': self.cod,
            'tipoNomenclador': self.nombreNomenclador,
            'nombre': self.nombre,
            'isActiv': self.isActiv
        }