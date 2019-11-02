from app.extensions import db
from app.model.hlmodel import Actividad, ActividadDetalle, Parametro, ActivDetalleParam
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


def siembraGfBarDB(parmIn):
    fchDesde=StringToDateTime(parmIn['fchDesde'])
    fchHasta=StringToDateTime(parmIn['fchHasta'])

    mesDesde=fchDesde.month
    mesHasta=fchHasta.month
    mes=[]
    for x in range(mesDesde, mesHasta+1):
        mes.append(x)

    
    codSiembra = 2
    codTipoSiembra = 50


    actividad = Actividad.query.filter(Actividad.cod == codSiembra).one()
    parametroObj = Parametro.query.filter(Parametro.cod == codTipoSiembra).one()
    parametroCant = Parametro.query.filter(Parametro.cod == 54).one()
    activDetalleList =  actividad.activDetalleList
    
    dtoPlantin=dict()
    dtoSemilla=dict()

    for m in mes:
            #print(dtoPlantin)
            dtoPlantin[m]=0
            dtoSemilla[m]=0
    #for detalle in activDetalleList:
        #if hlIsOkFch(detalle.fchActivDetalle,fchDesde,fchHasta):
            for detalle in activDetalleList:
                if m == detalle.fchActivDetalle.month:
                    
                    activDetalleParamList= detalle.paramList
                    for activDetalleParam in activDetalleParamList:

                        if activDetalleParam.param == parametroObj and activDetalleParam.valor=='plantin':
                            for itemAux in activDetalleParamList:
                                if itemAux.param == parametroCant:
                                    #print(itemAux.valor)
                                    dtoPlantin[m] = int(dtoPlantin[m]) + int(itemAux.valor)
                                    #print (dtoPlantin)
                                    exit
                                    
                        else:
                            if activDetalleParam.param == parametroObj and activDetalleParam.valor=='semilla':
                                for itemAux2 in activDetalleParamList:    
                                        if itemAux2.param == parametroCant:
                                            #print(itemAux2.valor)
                                            dtoSemilla[m] = int(dtoSemilla.get(m)) + int(itemAux2.valor)
                                            exit
                            
    #plantin
    keys = dtoPlantin.keys()
    data= []
    for key in keys:
        data.append(dtoPlantin[key])
    
    dtoAuxPlantin = dict(data=data,label='plantin')

    #semilla
    keys = dtoSemilla.keys()
    data= []
    for key in keys:
        data.append(dtoSemilla[key])
    
    dtoAuxSemilla = dict(data=data,label='semilla')

    dtoSiembra = []
    dtoSiembra.append(dtoAuxPlantin)
    dtoSiembra.append(dtoAuxSemilla)

    dtoReporte = dict(dataset=dtoSiembra,label=mes)
    return (dtoReporte)
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