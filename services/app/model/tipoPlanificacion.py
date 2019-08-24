from app.model.modelImport import *

class TipoPlanificacion(db.Model):
    __tablename__ = 'tipo_planificacion'
    codTipoPlanificacion = db.Column('cod_tipo_planificacion',Integer,primary_key = True,index = True)
    nombreTipoPlanificacion = db.Column('nombre_tipo_planificacion', String(32), nullable = False, unique = True)
    descTipoPlanificacion = db.Column('desc_tipo_planificacion', Text)
    isActiv = db.Column('is_activ', Boolean, nullable = False)

    def __init__(self, nombreTipoPlanificacion, descTipoPlanificacion,isActiv):
        self.nombreTipoPlanificacion = nombreTipoPlanificacion
        self.descTipoPlanificacion = descTipoPlanificacion
        self.isActiv = isActiv

    @staticmethod
    def from_json(json):
        tipoPlanificacion = TipoPlanificacion(
            nombreTipoPlanificacion=json.get('nombreTipoPlanificacion'),
            descTipoPlanificacion = json.get('descTipoPlanificacion'),
            isActiv=json.get('isActiv')
            )
        return tipoPlanificacion

    def to_json(self):
        return {
            'codTipoPlanificacion': self.codTipoPlanificacion,
            'nombreTipoPlanificacion': self.nombreTipoPlanificacion,
            'descTipoPlanificacion' : self.descTipoPlanificacion,
            'isActiv': self.isActiv
        }