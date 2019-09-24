from app.model.modelImport import *

class Recurso(db.Model):
    __tablename__ = 'recurso'
    cod = db.Column('cod_recurso',Integer,primary_key = True,index = True)
    nombre = db.Column('nombre_recurso', String(80), nullable = False, unique = True)
    isActiv = db.Column('is_activ', Boolean, nullable = False)
    tipoRecurso = db.Column('fk_tipo_recurso',Integer,ForeignKey('tipo_recurso.cod_tipo_recurso'),index = True)
    nombreNomenclador = "recurso"


    def __init__(self, nombre, isActiv,tipo):
        self.nombre = nombre
        self.isActiv = isActiv
        self.tipoRecurso = tipo

    @staticmethod
    def from_json(json):
        recurso = Recurso(
            nombre=json.get('nombre'),
            isActiv=json.get('isActiv')
            )
        return recurso

    def to_json(self):
        return {
            'id': self.cod,
            'tipoNomenclador': self.nombreNomenclador,
            'nombre': self.nombre,
            'isActiv': self.isActiv
        }