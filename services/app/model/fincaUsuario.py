from app.model.modelImport import *

class FincaUsuario(db.Model):
    __tablename__ = 'finca_usuario'
    codFinca = db.Column('fk_cod_finca',Integer,ForeignKey('finca.cod_finca'),primary_key = True)
    codUsuario=  db.Column('fk_cod_usuario',Integer,ForeignKey('usuario.cod_usuario_private'), primary_key = True)
    fchIni = db.Column('fch_ini', DateTime, default=datetime.datetime.now)
    fchFin = db.Column('fch_fin', DateTime, nullable= True) 
    isActiv = db.Column('is_activ',Boolean,nullable=False)

    finca = relationship("Finca", backref= 'fincaUsuarioList') #N->1
