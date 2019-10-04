from app.uses_cases.moduloConfiguracion.gestionarNomenclador import getNomencladoCod
from app.model import hlmodel
from app.repositorio.hlDb import saveEntidadSinCommit,Commit,deleteObject
from app.repositorio.repositorioRegistrarActividad import selectActivDetalle, selectActivDetalleCod, selectActivDetalleParm
from app.uses_cases.moduloConfiguracion.gestionarNomenclador import getNomencladoCod
from app.uses_cases.moduloConfiguracion.gestionarParametro import getParametroById
from app.api.helperApi.hlResponse import ResponseException, ResponseOk

from app.extensions import db
from datetime import datetime

def postRegistrarActiv(data):
    try:
        ##datos del json
        codActiv = data.get('codActividad')
        obs = data.get('observacion')
        imagenes = data.get('imagenes')
        parametros = data.get('parametros')
        fch = data.get('fchActivDetalle')

        activ = getNomencladoCod('actividad',codActiv)
        ##creación de la actividadDetalle
        detalleActiv = hlmodel.ActividadDetalle(observacion = obs,fchActivDetalle=fch)
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

def getRegistrarActiv():
    try:
        actividadDetalleList = selectActivDetalle()
        dtoDetalleList = []

        for detalle in actividadDetalleList:
            dtoDetalle = dict(
                codActivDetalle=detalle.codActivDetalle,
                fchActivDetalle= detalle.fchActivDetalle.strftime("%d/%m/%Y %H:%M:%S"),
                observacion=detalle.observacion)
            ##Actividad
            codActividad = detalle.actividad.cod
            nombreActividad = detalle.actividad.nombre
            dtoAuxActividad = dict(codActividad=codActividad,nombreActividad=nombreActividad)

            dtoDetalle['Actividad'] = dtoAuxActividad

            dtoDetalleList.append(dtoDetalle)

        return (dict(ActividadDetalle=dtoDetalleList))
    except Exception as e:
        return ResponseException(e)
 
def getRegistrarActivCod(codActivDetalle):
    try:
        detalle = selectActivDetalleCod(codActivDetalle)
        if not detalle:
            raise Exception('N','No existe actividad detalle con código ' + str(codActivDetalle))

        dtoDetalle = dict(
            codActivDetalle=detalle.codActivDetalle,
            fchActivDetalle= detalle.fchActivDetalle.strftime("%d/%m/%Y %H:%M:%S"),
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

        ##Imagenes
        imagenesList =  detalle.imgList
        dtoAuxImgList = []
        for img in imagenesList:
            dtoAuxImg = dict(dscImg=img.descripImg, base64=img.imgBase64)
            dtoAuxImgList.append(dtoAuxImg)
        dtoDetalle['Imagenes'] = dtoAuxImgList


        ##futuros datos que necesitmos  dtoDetalle['Futuros'] = x


        return (dict(dtoDetalle))      
    except Exception as e:
        return ResponseException(e)


def putRegistrarActiv(data,codActivDetalle):
    try:
        fchNew = data.get('fchActivDetalle')
        observacionNew = data.get('observacion')
        imagenesNew = data.get('imagenes')
        paramListNew = data.get('parametros')

        activDetalleObj = selectActivDetalleCod(codActivDetalle)
        if not activDetalleObj:
            raise Exception('N','No existe actividad detalle con código ' + str(codActivDetalle))

        if not activDetalleObj.fchActivDetalle == fchNew:
            activDetalleObj.fchActivDetalle=fchNew

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
        ##recupero las clases intermedias 
        actividad = getNomencladoCod('actividad',codActividad)
        paramListObj = actividad.actividadParamList

        dtoParametroFull = []
        for param in paramListObj:
            if param.isActiv: #filtro por activas
               codParametro = param.parametro.cod
               dtoAux= getParametroById(codParametro)
               print('acatoy')
               print(dtoAux)
               dtoParametroFull.append(dtoAux)
        

        return (dict(parametros=dtoParametroFull))
    except Exception as e:
        return ResponseException(e)