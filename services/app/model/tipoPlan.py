from app.model.modelImport import *

class TipoPlan(db.Model):
    __tablename__ = 'tipo_plan'
    codTipoPlan = db.Column('cod_tipo_plan', Integer,primary_key = True,index = True)
    nombreTipoPlan = db.Column('nombre_tipo_plan', String(60), nullable = False,  unique = True)
    isActiv = db.Column('is_activ', Boolean, nullable = False)
    
    #Relaciones OneToMany lado Many
    tipoPlanParam = relationship("TipoPlanParam")
    
    def __init__(self, nombreTipoPlan, isActiv):
        self.nombreTipoPlan = nombreTipoPlan
        self.isActiv = isActiv

    @staticmethod
    def from_json(json):
        tipoPlan = TipoPlan(
            nombreTipoPlan=json.get('nombreTipoPlan'),
            isActiv=json.get('isActiv')
            )
        return tipoPlan

    def to_json(self):
        return {
            'codTipoPlan': self.codTipoPlan,
            'nombreTipoPlan': self.nombreTipoPlan,
            'isActiv': self.isActiv
        }

