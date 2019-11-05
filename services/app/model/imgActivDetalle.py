from app.model.modelImport import *
import datetime

class ImgActivDetalle(db.Model):
    __tablename__ = 'img_activ_detalle'

    codImg  = db.Column('cod_img',Integer, primary_key = True,index = True)
    #nombreImg = db.Column('nombre_img',String, primary_key = True,index = True)
    descripImg =   db.Column('descrip_img', String(256))
    imgBase64 = db.Column('img_base64', String(999999), nullable = False)
    codActivDetalle = db.Column('fk_cod_activ_detalle',Integer,ForeignKey('actividad_detalle.cod_activ_detalle'),nullable=False) #relación
