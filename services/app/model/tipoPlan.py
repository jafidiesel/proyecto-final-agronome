from app.model.modelImport import *

class TipoPlanEntity(db.Model):
    __tablename__ = 'tipo_plan'
    codTipoPlan = db.Column('cod_tipo_plan', Integer,primary_key = True,index = Tru)
    nombreTipoPlan = db.Column('nombre_tipo_plan', String(60), nullable = False,  unique = True)
    isActiv = db.Column('is_activ', Boolean, nullable = False)

