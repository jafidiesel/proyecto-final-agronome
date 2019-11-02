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

