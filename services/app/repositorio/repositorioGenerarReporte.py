from app.extensions import db
from app.model.hlmodel import Actividad, ActividadDetalle, Parametro, ActivDetalleParam, Opcion, ParametroOpcion
from app.repositorio.repositorioRegistrarRecomendacion import selectRecomenActiv
from app.repositorio.repositorioLibroCampo import selectLibroCod
from datetime import datetime

def actividadGfBarDB(parmIn):
    fchDesde=StringToDateTime(parmIn['fchDesde'])
    fchHasta=StringToDateTime(parmIn['fchHasta'])
    codLibroCampo = parmIn['codLibroCampo']

    activDetalleList = hlActivDetalle(fchDesde,fchHasta)
    libroCampo = selectLibroCod(codLibroCampo)
    actividadList = Actividad.query.order_by(Actividad.cod).all()

    dtoActividad = dict()
    for actividad in actividadList:
        dtoActividad[actividad.nombre] = 0
        for detalle in activDetalleList:
            if detalle.actividad == actividad and detalle.libroCampoActivDetalle == libroCampo:
               dtoActividad[actividad.nombre] = int(dtoActividad.get(actividad.nombre)) + 1

    return dtoActividad


def recomendacionGfPieDB(parmIn):
    fchDesde = StringToDateTime(parmIn['fchDesde'])
    fchHasta = StringToDateTime(parmIn['fchHasta'])
    codLibroCampo = parmIn['codLibroCampo']
    activDetalleList = selectRecomenActiv(codLibroCampo) 

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
    codLibroCampo = parmIn['codLibroCampo']
    codActividad = parmIn['codActividad']
    codParamComboDual = parmIn['codParamComboDual']
    codParamIndicador = parmIn['codParamIndicador']
    codOpcionOne= parmIn['codOpcionOne']
    codOpcionTwo= parmIn['codOpcionTwo']

    
    ##recupero datos de la bd para realizar la logica
    actividad = Actividad.query.filter(Actividad.cod == codActividad).one()
    parametroObj = Parametro.query.filter(Parametro.cod == codParamComboDual).one()
    parametroCant = Parametro.query.filter(Parametro.cod == codParamIndicador).one()
    
    libroCampo = selectLibroCod(codLibroCampo)
    #activDetalleList =  libroCampo.activDetalleList
    activDetalleList =  actividad.activDetalleList
    

    mes = hlFchToMonth(fchDesde,fchHasta) #determinación de los meses
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


def actividadOptionGfPieDB(parmIn):
    fchDesde=StringToDateTime(parmIn['fchDesde'])
    fchHasta=StringToDateTime(parmIn['fchHasta'])
    codActividad = parmIn['codActividad']
    codParamComboOption = parmIn['codParamComboOption']


    #recupero los datos para poder generar el reporte
    actividad = Actividad.query.filter(Actividad.cod == codActividad).one()
    activDetalleList =  actividad.activDetalleList
    parametroObj = Parametro.query.filter(Parametro.cod == codParamComboOption).one()
    parametroOpcionObjList = parametroObj.paramOpcion
    
    ##defino las opciones
    opcionesList = []
    for paramOpcion in parametroOpcionObjList:
        opcionesList.append(paramOpcion.opcion.nombre)

    
    dtoOpcion = dict()
    for opcion in opcionesList:
        dtoOpcion[opcion] = 0

    #print (dtoOpcion)

    for activDetalle in activDetalleList:
        if hlIsOkFch(activDetalle.fchActivDetalle,fchDesde,fchHasta):
            activDetalleParamList = activDetalle.paramList
            for activDetalleParam in activDetalleParamList:
                if activDetalleParam.param ==parametroObj:
                    for opcion in opcionesList:
                        if activDetalleParam.valor == opcion:
                            dtoOpcion[opcion] = dtoOpcion.get(opcion) + 1 
                            exit

    return dtoOpcion





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

def hlFchToMonth(fchDesde,fchHasta):
    mesDesde=fchDesde.month
    mesHasta=fchHasta.month
    mes=[]
    for x in range(mesDesde, mesHasta+1):
        mes.append(x)
    
    return mes