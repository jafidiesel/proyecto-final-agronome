from app.model.modelImport import *


class Parametro(db.Model):
    __tablename__ = 'parametro'
    cod = db.Column('cod_parametro',Integer,primary_key = True,index = True)
    nombre = db.Column('nombre_parametro', String(32), nullable = False)
    isActiv = db.Column('is_activ', Boolean, nullable = False)
    codTipoParametro = db.Column('fk_cod_tipo_parametro',Integer,ForeignKey('tipo_parametro.cod_tipo_parametro'),index = True)
    codTipoDato = db.Column('fk_cod_tipo_dato',Integer,ForeignKey('tipo_dato.cod_tipo_dato'),index = True)
    #tipoParametroRef = relationship("TipoParametro", back_populates="parametroTipoRef",uselist=False)
    #datoParametroRef = relationship("TipoDato", back_populates="parametroDatoRef", uselist=False)
    #Relaciones OneToMany lado One
    #tipoParametro = relationship("TipoParametro", backref="parametroRef")
    #tipoParametro5 = relationship("TipoParametro", backref="parametroPruebaRef")
    #tipoDato = relationship("TipoDato", backref="parametroRef")
   
    
    def __init__(self, nombre, isActiv):
        self.nombre = nombre
        self.isActiv = isActiv
    

    @staticmethod
    def from_json(json):
        parametro = Parametro(
            nombre=json.get('nombre'),
            isActiv=json.get('isActiv')
            )

        return parametro

    def to_json(self):
        return {
            'cod': self.cod,
            'nombre': self.nombre,
            'isActiv': self.isActiv
        }

    def getObjetc(self):
        return self
