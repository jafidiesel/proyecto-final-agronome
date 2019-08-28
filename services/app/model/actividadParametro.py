from app.model.modelImport import *

class ActividadParametro(db.Model):
    __tablename__ = 'actividad_parametro'
    isActiv = db.Column('is_activ', Boolean, nullable = False)
    codParametro = db.Column('fk_cod_parametro',Integer,ForeignKey('parametro.cod_parametro'),index = True)
    codActividad = db.Column('fk_cod_actividad',Integer,ForeignKey('opcion.cod_actividad'),index = True)
    __table_args__ = (
        PrimaryKeyConstraint(codParametro, codActividad),
        {},
    )

    def __init__(self,isActiv):
        self.isActiv = isActiv

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