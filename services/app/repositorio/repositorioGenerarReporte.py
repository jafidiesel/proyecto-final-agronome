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


def actividadDualGfBarDB(parmIn):
    ##datos del entrada
    fchDesde=StringToDateTime(parmIn['fchDesde'])
    fchHasta=StringToDateTime(parmIn['fchHasta'])
    codActividad = parmIn['codActividad']
    codParamComboDual = parmIn['codParamComboDual']
    codParamIndicador = parmIn['codParamIndicador']
    codOpcionOne= parmIn['codOpcionOne']
    codOpcionTwo= parmIn['codOpcionTwo']

    
    ##recupero datos de la bd para realizar la logica
    actividad = Actividad.query.filter(Actividad.cod == codActividad).one()
    parametroObj = Parametro.query.filter(Parametro.cod == codParamComboDual).one()
    parametroCant = Parametro.query.filter(Parametro.cod == codParamIndicador).one()
    activDetalleList =  actividad.activDetalleList
    

    mes = hlFchToMomth(fchDesde,fchHasta) #determinación de los meses
    dtoOpcionOne=dict()
    dtoOpcionTwo=dict()

    for m in mes:
        dtoOpcionOne[m]=0
        dtoOpcionTwo[m]=0
        for detalle in activDetalleList:
            if m == detalle.fchActivDetalle.month: #si el detalle se hizo en este mes
                
                activDetalleParamList = detalle.paramList
                for activDetalleParam in activDetalleParamList:

                    if activDetalleParam.param == parametroObj and activDetalleParam.valor==codOpcionOne:
                        for itemAux in activDetalleParamList:
                            if itemAux.param == parametroCant:
                                valor=itemAux.valor.replace(',', '.',)
                                dtoOpcionOne[m] = float(dtoOpcionOne[m]) + float(valor)
                                exit
                                
                    else:
                        if activDetalleParam.param == parametroObj and activDetalleParam.valor==codOpcionTwo:
                            for itemAux2 in activDetalleParamList:    
                                    if itemAux2.param == parametroCant:
                                        valor=itemAux2.valor.replace(',', '.',)
                                        dtoOpcionTwo[m] = float(dtoOpcionTwo.get(m)) + float(valor)
                                        exit
                            
    
    ##armado del reporte bar
    
    keys = dtoOpcionOne.keys()
    data= []
    for key in keys:
        data.append(dtoOpcionOne[key])
    
    dtoAuxOpcionOne = dict(data=data,label=codOpcionOne)

    
    keys = dtoOpcionTwo.keys()
    data= []
    for key in keys:
        data.append(dtoOpcionTwo[key])
    
    dtoAuxOpcionTwo = dict(data=data,label=codOpcionTwo)

    dtoOpcion = []
    dtoOpcion.append(dtoAuxOpcionOne)
    dtoOpcion.append(dtoAuxOpcionTwo)

    dtoReporte = dict(dataset=dtoOpcion,label=mes)
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

def hlFchToMomth(fchDesde,fchHasta):
    mesDesde=fchDesde.month
    mesHasta=fchHasta.month
    mes=[]
    for x in range(mesDesde, mesHasta+1):
        mes.append(x)
    
    return mes