from app.model.modelImport import *

class Plan(db.Model):
    __tablename__ ='plan'
    codPlan = db.Column('cod_plan', Integer, primary_key = True, index = True)
    fchPlan = db.Column('fch_plan', DateTime, default = datetime.datetime.now, index = True)

    codTipoPlan = db.Column('fk_cod_tipo_plan',  Integer, ForeignKey('tipo_plan.cod_tipo_plan'),nullable=False)
    codUsuario = db.Column('fk_cod_usuario', Integer, ForeignKey('usuario.cod_usuario_private'), nullable=False)
    codGrupoCuadro = db.Column('fk_cod_grupo_cuadro', Integer, ForeignKey('grupo_cuadro.cod_grupo_cuadro'), nullable = True)
    
    tipoPlan = relationship('TipoPlan', backref= 'planList')
    paramList = relationship('PlanParam', backref = 'plan')
    usuario = relationship('Usuario')