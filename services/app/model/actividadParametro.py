from app.model.modelImport import *
#from app.model.hlmodel.parametro import Parametro
from app.model.hlmodel import Actividad, Parametro

class ActividadParametro(db.Model):
    __tablename__ = 'actividad_parametro'
    isActiv = db.Column('is_activ', Boolean, nullable = False)
    codParametro = db.Column('fk_cod_parametro',Integer,ForeignKey('parametro.cod_parametro'),index = True, primary_key = True)
    codActividad = db.Column('fk_cod_actividad',Integer,ForeignKey('actividad.cod_actividad'),index = True, primary_key = True)
   
    actividad = relationship("Actividad", backref="actividadParamList") #n->1
    parametro = relationship("Parametro", backref="paramActividadList") #n->1
    
    #def __init__(self,isActiv,parametro,actividad):
    #    self.isActiv = isActiv
    #    self.codParametro = parametro
    #    self.codActividad = actividad

    @staticmethod
    def from_json(json):
        actividadParametro = ActividadParametro(
            isActiv=json.get('isActiv')
            )
        return actividadParametro

    def to_json(self):
        return {
            'isActiv': self.isActiv
        }