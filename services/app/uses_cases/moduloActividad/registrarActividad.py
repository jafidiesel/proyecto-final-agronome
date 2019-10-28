from app.uses_cases.moduloConfiguracion.gestionarNomenclador import getNomencladoCod
from app.model import hlmodel
from app.repositorio.hlDb import saveEntidadSinCommit,Commit,deleteObject
from app.repositorio.repositorioRegistrarActividad import selectActivDetalle, selectActivDetalleCod, selectActivDetalleParm
from app.uses_cases.moduloConfiguracion.gestionarNomenclador import getNomencladoCod
from app.uses_cases.moduloConfiguracion.gestionarParametro import getParametroById
from app.api.helperApi.hlResponse import ResponseException, ResponseOk
from app.uses_cases.hlToDict import activDetalleToDict, activDetalleFullToDict, parametroListFullToDict
from app.extensions import db
from datetime import datetime

def postRegistrarActiv(data,currentUser):
    try:
        ##datos del json
        codActiv = data.get('codActividad')
        obs = data.get('observacion')
        imagenes = data.get('imagen')
        parametros = data.get('parametro')
        fch = data.get('fchActivDetalle')

        activ = getNomencladoCod('actividad',codActiv)
        ##creación de la actividadDetalle
        detalleActiv = hlmodel.ActividadDetalle(observacion = obs,fchActivDetalle=fch)
        detalleActiv.actividad = activ #asociación con actividad
        #asociacion con usuario
        detalleActiv.usuario = currentUser
        ##Parametros
        for param in parametros:
            codParam = param.get('codParam')
            valor = param.get('valor')
            parametro = getNomencladoCod('parametro',codParam)

            ##creación activDetalleParm
            activDetalleParm = hlmodel.ActivDetalleParam(valor=valor)
            activDetalleParm.param = parametro #asociación con parametro
            detalleActiv.paramList.append(activDetalleParm) # asociación con activDetalleParam

        ##imagenes
        for item in imagenes:
            dsc=item.get('dscImg')
            base64=item.get('base64')
            img = hlmodel.ImgActivDetalle(descripImg=dsc, imgBase64 = base64)
            detalleActiv.imgList.append(img)  #asociación con imgActivDetalle
        
        saveEntidadSinCommit(detalleActiv)
        Commit()

        return ResponseOk()
    except Exception as e:
        return ResponseException(e)

def getRegistrarActiv():
    try:
        actividadDetalleList = selectActivDetalle()
        dtoDetalleList = []

        for detalle in actividadDetalleList:
            dtoDetalle = activDetalleToDict(detalle)
            dtoDetalleList.append(dtoDetalle)

        return (dict(ActividadDetalle=dtoDetalleList))
    except Exception as e:
        return ResponseException(e)
 
def getRegistrarActivCod(codActivDetalle):
    try:
        detalle = selectActivDetalleCod(codActivDetalle)
        if not detalle:
            raise Exception('N','No existe actividad detalle con código ' + str(codActivDetalle))
        dtoDetalle = activDetalleFullToDict(detalle)

        return (dict(dtoDetalle))      
    except Exception as e:
        return ResponseException(e)


def putRegistrarActiv(data,currentUser,codActivDetalle):
    try:
        fchNew = data.get('fchActivDetalle')
        observacionNew = data.get('observacion')
        imagenesNew = data.get('imagen')
        paramListNew = data.get('parametro')

        activDetalleObj = selectActivDetalleCod(codActivDetalle)
        if not activDetalleObj:
            raise Exception('N','No existe actividad detalle con código ' + str(codActivDetalle))

        if not activDetalleObj.fchActivDetalle == fchNew:
            activDetalleObj.fchActivDetalle=fchNew

        if not activDetalleObj.observacion == observacionNew:
            activDetalleObj.observacion = observacionNew
        
        if not activDetalleObj.usuario == currentUser:
            activDetalleObj.usuario = currentUser

        for param in paramListNew:
            codParam = param.get('codParam')
            valorNew = param.get('valor')
            activDetalleParamObj=selectActivDetalleParm(codActivDetalle,codParam)
            if not activDetalleParamObj.valor == valorNew:
                activDetalleParamObj.valor = valorNew
        
        ##imagenes 
        imgList=activDetalleObj.imgList

        for img in imgList: # borro las imagenes para no comparar el archivo en base 64
            deleteObject(img)

        for imgNew in imagenesNew: #agrego las nuevas imagenes
            dsc=imgNew.get('dscImg')
            base=imgNew.get('base64')
            img=hlmodel.ImgActivDetalle(descripImg=dsc,imgBase64=base)
            activDetalleObj.imgList.append(img)


        saveEntidadSinCommit(activDetalleObj)
        Commit()

        return ResponseOk()
    except Exception as e:
        return ResponseException(e)

def deleteRegistrarActiv(data,codActivDetalle):
    try:
        activDetalleObj = selectActivDetalleCod(codActivDetalle)
        if not activDetalleObj:
            raise Exception('N','No existe actividad detalle con código ' + str(codActivDetalle))
        activDetalleObj.isEliminado= True
        saveEntidadSinCommit(activDetalleObj)
        Commit()
        return ResponseOk()
    except Exception as e:
        return ResponseException(e)


def getParametrosFull(codActividad):
    try:
        actividad = getNomencladoCod('actividad',codActividad)
        paramListObj = actividad.actividadParamList
        dtoParametroFull = parametroListFullToDict(paramListObj) 
        return (dict(parametros=dtoParametroFull))
    except Exception as e:
        return ResponseException(e)