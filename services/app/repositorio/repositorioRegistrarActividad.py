from app.extensions import db
from app.repositorio.repositorioLibroCampo import selectLibroCod
from app.model.hlmodel import ActividadDetalle, ActivDetalleParam, Parametro
from sqlalchemy import desc

def selectActivDetalle(): 
    objetos = ActividadDetalle.query.filter(ActividadDetalle.isEliminado==False).order_by(desc(ActividadDetalle.fchActivDetalle)).all()
    return  objetos 

def selectActivDetalleOrder(codLibroCampo): 
    libroCampo = selectLibroCod(codLibroCampo)
    objetos = ActividadDetalle.query.filter(ActividadDetalle.isEliminado==False and ActividadDetalle.libroCampoActivDetalle == libroCampo).order_by(desc(ActividadDetalle.fchActivDetalle)).all()
    return  objetos 

def selectActivDetalleCod(codActivDetalle):
    objeto = ActividadDetalle.query.filter(ActividadDetalle.codActivDetalle == codActivDetalle).first()
    return objeto

def selectActivDetalleParm(codActivDetalle,codParam):
    activDetalle = ActividadDetalle.query.filter(ActividadDetalle.codActivDetalle==codActivDetalle).first()
    parametro = Parametro.query.filter(Parametro.cod == codParam).first()

    activDetalleParam = ActivDetalleParam.query.filter(ActivDetalleParam.param==parametro).filter(ActivDetalleParam.activDetalle==activDetalle).first()
 
    return activDetalleParam