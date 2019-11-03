from app.repositorio.repositorioGenerarReporte import  actividadGfBarDB,recomendacionGfPieDB , actividadDualGfBarDB, actividadOptionGfPieDB

def actividadGfBar(data,currentUser):
    fchDesde = data.get('fchDesde')
    fchHasta = data.get('fchHasta')
    parmIn = dict (fchDesde =fchDesde, fchHasta=fchHasta)
    
    dtoActividad=actividadGfBarDB(parmIn)
    keys = dtoActividad.keys()
    dtoData= []
   
    for key in keys:
        data=[]
        data.append(dtoActividad[key])
        dtoAuxData=dict(data=data,label=key)
        dtoData.append(dtoAuxData)

    labelPpal = fchDesde + ' - ' + fchHasta

    dtoReporte= dict(dataset=dtoData,label=labelPpal)
    return dtoReporte


def recomendacionGfPie(data,currentUser):
    fchDesde = data.get('fchDesde')
    fchHasta = data.get('fchHasta')
    parmIn = dict (fchDesde =fchDesde, fchHasta=fchHasta)
    
    dtoRecom = recomendacionGfPieDB(parmIn)
    keys = dtoRecom.keys()
    number=[]
    labelPpal=[]
    for key in keys:
        number.append(dtoRecom[key])
        labelPpal.append(key)
    dtoAux=dict(number=number)

    dtoReporte= dict(dataset=dtoAux,label=labelPpal)
    return dtoReporte


def actividadDualGfBar(data,currentUser):
    fchDesde = data.get('fchDesde')
    fchHasta = data.get('fchHasta')
    codActividad = data.get('codActividad')
    codParamComboDual = data.get('codParamComboDual')
    codOpcionOne = data.get('codOpcionOne')
    codOpcionTwo = data.get('codOpcionTwo')
    codParamIndicador = data.get('codParamIndicador')


    parmIn = dict(
        fchDesde = fchDesde,
        fchHasta = fchHasta,
        codActividad = codActividad,
        codParamComboDual = codParamComboDual,
        codParamIndicador = codParamIndicador,
        codOpcionOne = codOpcionOne,
        codOpcionTwo = codOpcionTwo
        )
    dtoReporte=actividadDualGfBarDB(parmIn)
    return dtoReporte


def actividadOptionGfPie(data,currentUser):
    fchDesde = data.get('fchDesde')
    fchHasta = data.get('fchHasta')
    codActividad = data.get('codActividad')
    codParamComboOption = data.get('codParamComboOption')


    parmIn = dict(
        fchDesde = fchDesde,
        fchHasta = fchHasta,
        codActividad = codActividad,
        codParamComboOption = codParamComboOption,
        )

    dtoOpcion = actividadOptionGfPieDB(parmIn)

    keys = dtoOpcion.keys()
    values = dtoOpcion.values()

    total = 0
    for value in values:
        total = total + value

    if total>0:
        porcentaje = 100/total
    else:
        porcentaje = 0

    number=[]
    label=[]
    for key in keys:
        number.append(dtoOpcion[key]*porcentaje)
        label.append(key) 

    data=dict(number=number)
    dtoReporte = dict(dataset=data,label=label)

    return dtoReporte