from app.uses_cases.moduloConfiguracion.gestionarParametro import getParametroById 
##Parametro
def parametroToDict(parametro):
    dtoParametro = dict(
        codParametro    = parametro.param.cod,
        nombreParametro = parametro.param.nombre,
        valor           = parametro.valor
    )
    return dtoParametro


def parametroListToDict(paramList):
    dtoParametroList= []
    for parametro in paramList:
        dtoParametro = parametroToDict(parametro)
        dtoParametroList.append(dtoParametro)
    return dtoParametroList


def parametroListFullToDict(paramList): #este solo se usa para la estructura ojo
    dtoParametroList = []
    for param in paramList:
        if param.isActiv:
            codParametro = param.parametro.cod
            dtoAuxParam  = getParametroById(codParametro)
            dtoParametroList.append(dtoAuxParam)
    return dtoParametroList


##Actividad
def actividadToDict(actividad):
    dtoActividad = dict(
        codActividad = actividad.cod,
        nombreActividad = actividad.nombre
    )
    return dtoActividad

def activDetalleToDict(activDetalle):
    dtoActivDetalle = dict (
        codActivDetalle = activDetalle.codActivDetalle,  
        fchActivDetalle = activDetalle.fchActivDetalle.strftime("%d-%m-%Y %H:%M:%S"),
        observacion     = activDetalle.observacion,
        isEliminado     = activDetalle.isEliminado
    )

    dtoActivDetalle['actividad'] = actividadToDict(activDetalle.actividad)
    return dtoActivDetalle 

def imgListToDict(imgList):
    dtoImagenList = []
    for img in imgList:
        dtoImagen = dict(
            dscImg = img.descripImg, 
            base64 = img.imgBase64
            )
        dtoImagenList.append(dtoImagen)
    return dtoImagenList


def activDetalleFullToDict(activDetalle):
    dtoActivDetalle = activDetalleToDict(activDetalle)
    dtoActivDetalle['parametro'] = parametroListToDict(activDetalle.paramList)
    dtoActivDetalle['imagen']    = imgListToDict(activDetalle.imgList)
    dtoActivDetalle['usuario']   = usuarioToDict(activDetalle.usuario)
    return dtoActivDetalle


##Recomendacion
def recomendacionToDict(recomendacion):
    dtoRecomendacion = dict(
        codRecomendacion    = recomendacion.cod,
        nombreRecomendacion = recomendacion.nombre
    )
    return dtoRecomendacion 

def recomDetalleToDict(recomDetalle):
    dtoRecomDetalle = dict(
        codRecomDetalle = recomDetalle.codRecomDetalle, 
        fchRecomDetalle = recomDetalle.fchRecomDetalle.strftime("%d-%m-%Y %H:%M:%S"), 
        observacion     = recomDetalle.observacion     
    )
    dtoRecomDetalle['recomendacion'] = recomendacionToDict(recomDetalle.recomendacion)
    return dtoRecomDetalle

def recomDetalleFullToDict(recomDetalle):
    dtoRecomDetalle = recomDetalleToDict(recomDetalle)
    dtoRecomDetalle['parametro']     = parametroListToDict(recomDetalle.paramList)
    dtoRecomDetalle['usuario']       = usuarioToDict(recomDetalle.usuario) 
    dtoRecomDetalle['analisis']      = analisisListFullToDicc(recomDetalle.analisisList)
    
    return dtoRecomDetalle



##Usuario
def usuarioToDict(usuario):
    dtoUsuario = dict(
        codUsuario    = usuario.codPrivate,
        nombreUsuario = usuario.nombre + ' ' +usuario.apellido
    )
    return dtoUsuario



#Analisis
def tipoAnalisisToDict(tipoAnalisis):
    dtoTipoAnalisis = dict( 
        codTipoAnalisis    = tipoAnalisis.cod,
        nombreTipoAnalisis = tipoAnalisis.nombre
    )
    return dtoTipoAnalisis

def analisisToDicc(analisis):
    dtoAnalisis= dict(
        codAnalisis = analisis.codAnalisis,
        fhcAnalisis = analisis.fchAnalisis.strftime("%d-%m-%Y %H:%M:%S"),
    )

    dtoAnalisis['tipoAnalsis'] = tipoAnalisisToDict(analisis.tipoAnalisis)
    return dtoAnalisis

def analisisFullToDicc(analisis):
    dtoAnalisis = analisisToDicc(analisis)
    dtoAnalisis['parametro'] = parametroListToDict(analisis.paramList)
    dtoAnalisis['usuario']   = usuarioToDict(analisis.usuario)
    return dtoAnalisis

def analisisListFullToDicc(analisisList):
    dtoAnalisisList=[]
    for analisis in analisisList:
        dtoAnalisis = analisisFullToDicc(analisis)
        dtoAnalisisList.append(dtoAnalisis)
    
    return dtoAnalisisList


#Plan
def tipoPlanToDict(tipoPlan):
    dtoTipoPlan = dict(
        codTipoPlan    = tipoPlan.cod,
        nombreTipoPlan = tipoPlan.nombre
    )  
    return dtoTipoPlan


def planToDict(plan):
    dtoPlan = dict(
        codPlan     = plan.codPlan,
        fhcPlan = plan.fchPlan.strftime("%d-%m-%Y %H:%M:%S"),
    )
    dtoPlan['tipoPlan'] = tipoPlanToDict(plan.tipoPlan)

    return dtoPlan


def planFullToDict(plan):
    dtoPlan = planToDict(plan)
    dtoPlan ['parametro'] = parametroListToDict(plan.paramList)
    dtoPlan ['usuario']   = usuarioToDict(plan.usuario)
    return dtoPlan
