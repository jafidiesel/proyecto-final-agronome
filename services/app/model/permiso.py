from app.model.modelImport import *

class Permiso(db.Model):
    __tablename__ = 'permiso'
    cod = db.Column('cod_permiso',  Integer,primary_key = True,index = True)
    nombre = db.Column('nombre_permiso', String(80), nullable = False,  unique = True)
    isActiv = db.Column('is_activ', Boolean, nullable = False)
    
    nombreNomenclador = "permiso"

    def __init__(self, nombre, isActiv):
        self.nombre = nombre
        self.isActiv = isActiv

    @staticmethod
    def from_json(json):
        permiso = Permiso(
            nombre=json.get('nombre'),
            isActiv=json.get('isActiv')
            )
        return permiso

    def to_json(self):
        return {
            'id': self.cod,
            'tipoNomenclador': self.nombreNomenclador,
            'nombre': self.nombre,
            'isActiv': self.isActiv
        }