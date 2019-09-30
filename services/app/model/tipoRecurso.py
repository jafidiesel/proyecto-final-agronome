from app.model.modelImport import *

class TipoRecurso(db.Model):
    __tablename__ = 'tipo_recurso'
    cod = db.Column('cod_tipo_recurso',Integer,primary_key = True,index = True)
    nombre = db.Column('nombre_tipo_recurso', String(80), nullable = False, unique = True)
    isActiv = db.Column('is_activ', Boolean, nullable = False)
    
    recursos = relationship('Recurso',backref= 'tipoRe',lazy='dynamic')


    nombreNomenclador = "tipoRecurso"
    def __init__(self, nombre, isActiv):
        self.nombre = nombre
        self.isActiv = isActiv

    @staticmethod
    def from_json(json):
        tipoRecurso = TipoRecurso(
            nombre=json.get('nombre'),
            isActiv=json.get('isActiv')
            )
        return tipoRecurso

    def to_json(self):
        return {
            'cod': self.cod,
            'tipoNomenclador': self.nombreNomenclador,
            'nombre': self.nombre,
            'isActiv': self.isActiv
        }