from app.model.modelImport import *

class Recomendacion(db.Model):
    __tablename__ = 'recomendacion'
    codRecomendacion = db.Column('cod_recomendacion',Integer,primary_key = True,index = True)
    nombreRecomendacion = db.Column('nombre_recomendacion', String(32), nullable = False, unique = True)
    isActiv = db.Column('is_activ', Boolean, nullable = False)

    nombreNomenclador = "recomendacion"


    def __init__(self, nombreRecomendacion, isActiv):
        self.nombreRecomendacion = nombreRecomendacion
        self.isActiv = isActiv

    @staticmethod
    def from_json(json):
        recomendacion = Recomendacion(
            nombreRecomendacion=json.get('nombre'),
            isActiv=json.get('isActiv')
            )
        return recomendacion

    def to_json(self):
        return {
            'id': self.codRecomendacion,
            'tipoNomenclador': self.nombreNomenclador,
            'nombre': self.nombreRecomendacion,
            'isActiv': self.isActiv
        }