from app.model.modelImport import *

class TipoDato(db.Model):
    __tablename__ = 'tipo_dato'
    codTipoDato = db.Column('cod_tipo_dato',Integer,primary_key = True,index = True)
    nombreTipoDato = db.Column('nombre_tipo_dato', String(32), nullable = False, unique = True)
    isActiv = db.Column('is_activ', Boolean, nullable = False)

    #Relaciones OneToMany lado Many
    parametro = relationship("Parametro")

    def __init__(self, nombreTipoDato, isActiv):
        self.nombreTipoDato = nombreTipoDato
        self.isActiv = isActiv

    @staticmethod
    def from_json(json):
        tipoDato = TipoDato(
            nombreTipoDato=json.get('nombreTipoDato'),
            isActiv=json.get('isActiv')
            )
        return tipoDato

    def to_json(self):
        return {
            'codTipoDato': self.codTipoDato,
            'nombreTipoDato': self.nombreTipoDato,
            'isActiv': self.isActiv
        }