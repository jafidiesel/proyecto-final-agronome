from app.model.modelImport import *

class ParametroOpcion(db.Model):
    __tablename__ = 'parametro_opcion'
    isActiv = db.Column('is_activ', Boolean, nullable = False)
    codParametro = db.Column('fk_cod_parametro',Integer,ForeignKey('parametro.cod_parametro'),index = True)
    codOpcion = db.Column('fk_cod_opcion',Integer,ForeignKey('opcion.cod_opcion'),index = True)
    __table_args__ = (
        PrimaryKeyConstraint(codParametro, codOpcion),
        {},
    )


    def __init__(self,isActiv):
        self.isActiv = isActiv

    @staticmethod
    def from_json(json):
        parametroOpcion = ParametroOpcion(
            isActiv=json.get('isActiv')
            )
        return parametroOpcion

    def to_json(self):
        return {
            'isActiv': self.isActiv
        }