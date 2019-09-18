from app.model.modelImport import *
from app.model.hlmodel import Parametro,Opcion

class ParametroOpcion(db.Model):
    __tablename__ = 'parametro_opcion'
    isActiv = db.Column('is_activ', Boolean, nullable = False)
    codParametro = db.Column('fk_cod_parametro',Integer,ForeignKey('parametro.cod_parametro'),index = True, primary_key = True)
    codOpcion = db.Column('fk_cod_opcion',Integer,ForeignKey('opcion.cod_opcion'),index = True,  primary_key = True)
      
    def __init__(self,isActiv,parametro,opcion):
        self.isActiv = isActiv
        self.codParametro = parametro
        self.codOpcion = opcion
        
    #parametro = relationship(Parametro,backref = "parametroOpcion")
    #print("Paramtro relationship")
    
    #opcion = relationship(Opcion,backref = "parametroOpcion")
    #print("Opcion relationship")

   

    @staticmethod
    #def from_json(json):
    #    parametroOpcion = ParametroOpcion(
    #        isActiv=json.get('isActiv')
    #       )
    #    print(parametroOpcion.isActiv)
    #    return parametroOpcion

    def to_json(self):
        return {
            'isActiv': self.isActiv
        }