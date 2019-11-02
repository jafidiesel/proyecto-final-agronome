from app.extensions import db
from app.model.hlmodel import Actividad, ActividadDetalle
from app.repositorio.repositorioRegistrarRecomendacion import selectRecomenActiv
from datetime import datetime
def actividadGfBarDB(parmIn):
    fchDesde=StringToDateTime(parmIn['fchDesde'])
    fchHasta=StringToDateTime(parmIn['fchHasta'])
    
    activDetalleList = hlActivDetalle(fchDesde,fchHasta)
    actividadList = Actividad.query.order_by(Actividad.cod).all()

    dtoActividad = dict()
    for actividad in actividadList:
        dtoActividad[actividad.nombre] = 0
        for detalle in activDetalleList:
            if detalle.actividad == actividad:
               dtoActividad[actividad.nombre] = int(dtoActividad.get(actividad.nombre)) + 1

    return dtoActividad


def recomendacionGfPieDB(parmIn):
    fchDesde=StringToDateTime(parmIn['fchDesde'])
    fchHasta=StringToDateTime(parmIn['fchHasta'])

    activDetalleList = selectRecomenActiv() #enviar luego la finca

    activRecomendadas = 0
    activARecomendar = 0
    for detalle in activDetalleList:
        if hlIsOkFch(detalle.fchActivDetalle,fchDesde,fchHasta):
            if  detalle.codRecomDetalle == None:
                activARecomendar = activARecomendar + 1
            else:
                activRecomendadas = activRecomendadas +1
    

    dtoRecomen =dict(activARecomendar=activARecomendar,activRecomendadas=activRecomendadas)
    
    return dtoRecomen




#helper

#Retorna los detalles entre 2 fechas
def hlActivDetalle(fchDesde,fchHasta):
    objetos = ActividadDetalle.query.filter(ActividadDetalle.fchActivDetalle >= fchDesde).filter(ActividadDetalle.fchActivDetalle <= fchHasta).all()    
    return objetos

def hlIsOkFch(fch,fchDesde,fchHasta):
    isOk=False
    if fch>=fchDesde and fch<=fchHasta:
        isOk=True 
    return isOk

def StringToDateTime(auxFch):
    fch=datetime.strptime(auxFch, '%Y-%m-%d %H:%M')
    return fch