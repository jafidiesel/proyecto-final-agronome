from app.model.modelImport import *

class Analisis(db.Model):
    __tablename__ ='analisis'
    codAnalisis = db.Column('cod_analisis',Integer, primary_key = True, index = True)
    fchAnalisis = db.Column ('fch_analisis', DateTime, default = datetime.datetime.now, index = True)

    codTipoAnalisis = db.Column('fk_cod_tipo_analisis', Integer, ForeignKey('tipo_analisis.cod_tipo_analisis'), nullable=False)
    codUsuario = db.Column('fk_cod_usuario', Integer, ForeignKey('usuario.cod_usuario_private'), nullable = False)

    #fk nullables
    codRecomDetalle = db.Column('fk_cod_recom_detalle', Integer, ForeignKey('recomendacion_detalle.cod_recom_detalle'), nullable = True)  #recomendación

    #agregar planicifación y/o grupo cuadro


    tipoAnalisis = relationship("TipoAnalisis", backref = 'analisisList')
    
    paramList = relationship('AnalisisParam', backref = 'analisis')

    usuario = relationship('Usuario')