from app.model.modelImport import *

class EstadoPlanificacion(db.Model):
    __tablename__ = 'estado_planificacion'
    codEstadoPlanificacion = db.Column('cod_estado_planificacion', Integer,primary_key = True,index = True)
    nombreEstadoPlanificacion = db.Column('nombre_estado_planificacion', String(60), nullable = False,  unique = True)
    isActiv = db.Column('is_activ', Boolean, nullable = False)
    

    def __init__(self, nombreEstadoPlanificacion,isActiv):
        
        self.nombreEstadoPlanificacion = nombreEstadoPlanificacion
        self.isActiv = isActiv

    @staticmethod
    def from_json(json):
        estadoPlanificacion = EstadoPlanificacion(
            nombreEstadoPlanificacion=json.get('nombreEstadoPlanificacion'),
            isActiv=json.get('isActiv')
            )
        return estadoPlanificacion

    def to_json(self):
        return {
            'codEstadoPlanificacion': self.codEstadoPlanificacion,
            'nombreEstadoPlanificacion': self.nombreEstadoPlanificacion,
            'isActiv': self.isActiv
        }