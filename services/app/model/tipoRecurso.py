from app.model.modelImport import *

class TipoRecurso(db.Model):
    __tablename__ = 'tipo_Recurso'
    codTipoRecurso = db.Column('cod_tipo_recurso',Integer,primary_key = True,index = True)
    nombreTipoRecurso = db.Column('nombre_tipo_recurso', String(32), nullable = False, unique = True)
    isActiv = db.Column('is_activ', Boolean, nullable = False)
    nombreNomenclador = "tipoRecurso"


    def __init__(self, nombreTipoRecurso, isActiv):
        self.nombreTipoRecurso = nombreTipoRecurso
        self.isActiv = isActiv

    @staticmethod
    def from_json(json):
        tipoRecurso = TipoRecurso(
            nombreTipoRecurso=json.get('nombre'),
            isActiv=json.get('isActiv')
            )
        return tipoRecurso

    def to_json(self):
        return {
            'id': self.codTipoRecurso,
            'tipoNomenclador': self.nombreNomenclador,
            'nombre': self.nombreTipoRecurso,
            'isActiv': self.isActiv
        }