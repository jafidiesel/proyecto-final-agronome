from app.uses_cases.moduloConfiguracion.gestionarNomenclador import getNomencladoCod
from app.model import hlmodel
from app.repositorio.hlDb import saveEntidad, saveEntidadSinCommit,Rollback,Commit,selectByCod, addObject, selectAll
from app.api.helperApi.hlResponse import ResponseException, ResponseOk
##borrar

from flask import jsonify
from app.extensions import db

def postRegistrarActiv(data):
    try:
        ##datos del json
        codActiv = data.get('idActividad')
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
    #nActividad = hlmodel.Actividad
    nActividad = getNomencladoCod('actividad',1)

    objetos = nActividad.activDetalleList 

    #print (nActividad)
    
    for o in objetos:
        print(o.observacion)
        imgs= o.imgList

        for i in imgs:
            print (i.codImg)
            base64 = i.imgBase64
    return (base64)