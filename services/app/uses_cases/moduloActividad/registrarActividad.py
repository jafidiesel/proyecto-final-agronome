from app.uses_cases.moduloConfiguracion.gestionarNomenclador import getNomencladoCod
from app.model import hlmodel
from app.repositorio.hlDb import saveEntidad, saveEntidadSinCommit,Rollback,Commit,selectByCod, addObject, selectAll, deleteObject
from app.repositorio.repositorioRegistrarActividad import selectActivDetalle, selectActivDetalleCod, selectActivDetalleParm

from app.api.helperApi.hlResponse import ResponseException, ResponseOk
##borrar

from flask import jsonify
from app.extensions import db
from datetime import datetime

def postRegistrarActiv(data):
    try:
        ##datos del json
        codActiv = data.get('codActividad')
        obs = data.get('observacion')
        imagenes = data.get('imagenes')
        parametros = data.get('parametros')


        activ = getNomencladoCod('actividad',codActiv)
        ##creación de la actividadDetalle
        detalleActiv = hlmodel.ActividadDetalle(observacion = obs)
        detalleActiv.actividad = activ #asociación con actividad

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

def getRegistrarActiv(data):
    actividadDetalleList = selectActivDetalle()
    dtoDetalleList = []

    for detalle in actividadDetalleList:
        dtoDetalle = dict(
            codActivDetalle=detalle.codActivDetalle,
            fchActivDetalle= detalle.fchActivDetalle.strftime("%d/%m/%Y, %H:%M:%S"),
            observacion=detalle.observacion)
        ##Actividad
        codActividad = detalle.actividad.cod
        nombreActividad = detalle.actividad.nombre
        dtoAuxActividad = dict(codActividad=codActividad,nombreActividad=nombreActividad)

        dtoDetalle['Actividad'] = dtoAuxActividad

        ##Parametros
        parametrosList = detalle.paramList    
        dtoAuxParametroList = []
        for parametro in parametrosList:
            #parametro.param.cod
            dtoAuxParametro =dict(codParamtro=parametro.param.cod, nombreParametro=parametro.param.nombre,valor = parametro.valor)
            dtoAuxParametroList.append(dtoAuxParametro)

        dtoDetalle['Parametros'] = dtoAuxParametroList

        dtoDetalleList.append(dtoDetalle)

        ##Imagenes
        imagenesList =  detalle.imgList
        dtoAuxImgList = []
        for img in imagenesList:
            dtoAuxImg = dict(dscImg=img.descripImg, base64=img.imgBase64)
            dtoAuxImgList.append(dtoAuxImg)

        dtoDetalle['Imagenes'] = dtoAuxImgList

    return (dict(ActividadDetalle=dtoDetalleList))


def putRegistrarActiv(data,codActivDetalle):
    observacionNew = data.get('observacion')
    imagenesNew = data.get('imagenes')
    paramListNew = data.get('parametros')

    activDetalleObj = selectActivDetalleCod(codActivDetalle)

    if not activDetalleObj.observacion == observacionNew:
        activDetalleObj.observacion = observacionNew
    
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

    return(dict(codActiv=activDetalleObj.actividad.cod,obs= activDetalleObj.observacion))


def deleteRegistrarActiv(data,codActivDetalle):
    activDetalleObj = selectActivDetalleCod(codActivDetalle)
    activDetalleObj.isEliminado= True
    saveEntidadSinCommit(activDetalleObj)
    Commit()
    return('ok')