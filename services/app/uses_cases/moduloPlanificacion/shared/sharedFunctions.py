from app.model.hlmodel import TipoCultivo

def tipoCultivoToDict(tipoCultivo):
    dtoTipoCultivo = dict(
        cod = tipoCultivo.cod,
        nombre = tipoCultivo.nombre,
        isActiv = tipoCultivo.isActiv
    )
    return dtoTipoCultivo

def tipoCultivoListToDict(tipoCultivoList):
    dtoTipoCultivoList= []
    for tipoCultivo in tipoCultivoList:
        dtoTipoCultivo = tipoCultivoToDict(tipoCultivo)
        dtoTipoCultivoList.append(dtoTipoCultivo)
    return dtoTipoCultivoList

def planificacionToDict(planificacionRst):
    #Leer entidades asociadas
    estadoRst = planificacionRst.estadoPlanificacion
    tipoRst = planificacionRst.tipoPlanificacion
    grupoListRst = planificacionRst.grupoCuadroList
    #Armado Dto
    estadoDict = estadoRst.__dict__
    tipoDict = tipoRst.__dict__
    
    estadoDict.pop('_sa_instance_state', None)
    tipoDict.pop('_sa_instance_state', None)
    planificacionRst.pop('_sa_instance_state', None)

    for grupo in grupoListRst:
        pass

    


