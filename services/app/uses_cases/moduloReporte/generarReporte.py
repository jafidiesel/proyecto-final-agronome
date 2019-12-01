from app.repositorio.repositorioGenerarReporte import  actividadGfBarDB,recomendacionGfPieDB , actividadDualGfBarDB, actividadOptionGfPieDB

def actividadGfBar(data,currentUser):
    fchDesde = data.get('fchDesde')
    fchHasta = data.get('fchHasta')
    codLibroCampo = data.get('codLibroCampo')

    parmIn   = dict (fchDesde =fchDesde, fchHasta=fchHasta, codLibroCampo = codLibroCampo)
    
    dtoData = actividadGfBarDB(parmIn)
    nameData = 'data'

    dtoReporte = toDtoReporte(dtoData,nameData,fchDesde,fchHasta)
    return dtoReporte


def recomendacionGfPie(data,currentUser):
    fchDesde = data.get('fchDesde')
    fchHasta = data.get('fchHasta')
    codLibroCampo = data.get('codLibroCampo')
    parmIn = dict (fchDesde =fchDesde, fchHasta=fchHasta, codLibroCampo = codLibroCampo)
    
    dtoData = recomendacionGfPieDB(parmIn)
    nameData = 'number'
    
    dtoReporte = toDtoReporte(dtoData,nameData,fchDesde,fchHasta)
    return dtoReporte


def actividadDualGfBar(data,currentUser):
    fchDesde = data.get('fchDesde')
    fchHasta = data.get('fchHasta')
    codLibroCampo = data.get('codLibroCampo')
    codActividad = data.get('codActividad')
    codParamComboDual = data.get('codParamComboDual')
    codOpcionOne = data.get('codOpcionOne')
    codOpcionTwo = data.get('codOpcionTwo')
    codParamIndicador = data.get('codParamIndicador')


    parmIn = dict(
        fchDesde = fchDesde,
        fchHasta = fchHasta,
        codLibroCampo = codLibroCampo,
        codActividad = codActividad,
        codParamComboDual = codParamComboDual,
        codParamIndicador = codParamIndicador,
        codOpcionOne = codOpcionOne,
        codOpcionTwo = codOpcionTwo
        )

    dtoReporte=actividadDualGfBarDB(parmIn)

    dtoFecha = fchToDtoFfch(fchDesde,fchHasta)
    dtoReporte['fecha'] = dtoFecha #se agrega de esta manera porque la logica se resuelve en actividadDualGfBarDB y aca solo le seteamos al fecha
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

    dtoData = actividadOptionGfPieDB(parmIn)
    keys = dtoData.keys()
    values = dtoData.values()

    #porcentaje
    total = 0
    for value in values:
        total = total + value

    if total>0:
        porcentaje = 100/total
    else:
        porcentaje = 0

    for key in keys:
        dtoData[key] = dtoData.get(key) * porcentaje

    nameData='number'

    dtoReporte = toDtoReporte(dtoData,nameData,fchDesde,fchHasta)
    return dtoReporte


def fchToDtoFfch(fchDesde,fchHasta):
    dtoFecha = dict(
        fchDesde=fchDesde,
        fchHasta=fchHasta
        )
    return dtoFecha

def toDtoReporte(dtoData,nameData,fchDesde,fchHasta):
    dtoFecha = fchToDtoFfch(fchDesde,fchHasta)
    keys     = dtoData.keys()
    label    = []
    data     = []

    for key in keys:
        data.append(dtoData[key])
        label.append(key)

    dtoDataset=dict()
    dtoDataset[nameData]=data #nameData se encuentra definido en la documentación de ng2chart
    dtoReporte = dict(dataset=dtoDataset,label=label,fecha=dtoFecha)

    return dtoReporte