from app.model.modelImport import *
from app.model.hlmodel import *

class TipoPlan(db.Model):
    __tablename__ = 'tipo_plan'
    cod = db.Column('cod_tipo_plan', Integer,primary_key = True,index = True)
    nombre = db.Column('nombre_tipo_plan', String(60), nullable = False,  unique = True)
    isActiv = db.Column('is_activ', Boolean, nullable = False)
    
    #Relaciones OneToMany lado Many
    tipoPlanParam = relationship("TipoPlanParam")
    nombreNomenclador = "tipoPlan"

    def __init__(self, nombre, isActiv):
        self.nombre = nombreTipoPlan
        self.isActiv = isActiv

    @staticmethod
    def from_json(json):
        tipoPlan = TipoPlan(
            nombre=json.get('nombre'),
            isActiv=json.get('isActiv')
            )
        return tipoPlan

    def to_json(self):
        return {
            'id': self.cod,
            'tipoNomenclador': self.nombreNomenclador,
            'nombre': self.nombre,
            'isActiv': self.isActiv
        }

