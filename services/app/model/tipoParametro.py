from app.model.modelImport import *

class TipoParametro(db.Model):
    __tablename__ = 'tipo_parametro'
    codTipoParametro = db.Column('cod_tipo_parametro',Integer,primary_key = True,index = True)
    nombreTipoParametro = db.Column('nombre_tipo_parametro', String(32), nullable = False, unique = True)
    isActiv = db.Column('is_activ', Boolean, nullable = False)
      
    #Relaciones OneToMany lado Many
    parametro = relationship("Parametro")

    def __init__(self, nombreTipoParametro, isActiv):
        self.nombreTipoParametro = nombreTipoParametro
        self.isActiv = isActiv

    @staticmethod
    def from_json(json):
        tipoParametro = TipoParametro(
            nombreTipoParametro=json.get('nombreTipoParametro'),
            isActiv=json.get('isActiv')
            )
        return tipoParametro

    def to_json(self):
        return {
            'codTipoParametro': self.codTipoParametro,
            'nombreTipoParametro': self.nombreTipoParametro,
            'isActiv': self.isActiv
        }