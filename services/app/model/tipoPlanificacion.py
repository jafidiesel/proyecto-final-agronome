from app.model.modelImport import *

class TipoPlanificacion(db.Model):
    __tablename__ = 'tipo_planificacion'
    codTipoPlanificacion = db.Column('cod_tipo_planificacion',Integer,primary_key = True,index = True)
    nombreTipoPlanificacion = db.Column('nombre_tipo_planificacion', String(32), nullable = False, unique = True)
    isActiv = db.Column('is_activ', Boolean, nullable = False)
    nombreNomenclador = "tipoPlanificacion"    

    def __init__(self, nombreTipoPlanificacion,isActiv):
        self.nombreTipoPlanificacion = nombreTipoPlanificacion
        self.isActiv = isActiv

    @staticmethod
    def from_json(json):
        tipoPlanificacion = TipoPlanificacion(
            nombreTipoPlanificacion=json.get('nombre'),            
            isActiv=json.get('isActiv')
            )
        return tipoPlanificacion

    def to_json(self):
        return {
            'id': self.codTipoPlanificacion,
            'tipoNomenclador': self.nombreNomenclador,
            'nombre': self.nombreTipoPlanificacion,
            'isActiv': self.isActiv
        }