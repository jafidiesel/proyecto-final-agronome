from flask import jsonify
from app.repositorio.hlDb import saveEntidadSinCommit, Commit,Rollback, selectAllisActiv
from app.repositorio.repositorioGestionarAsociacion import cantAsociaciones
from app.model import hlmodel
from app.uses_cases.moduloConfiguracion.gestionarNomenclador import getNomencladoCod
from app.api.helperApi.hlResponse import ResponseException, ResponseOk
import json

modelos = { 
"actividadParametro":hlmodel.ActividadParametro,
"recomendacionParametro": hlmodel.RecomendacionParametro,
"tipoAnalisisParam":hlmodel.TipoAnalisisParam,
"tipoPlanParam": hlmodel.TipoPlanParam
}

nomenclador = { ##para detectar la entidad y usar el getNomencladoCod
"actividadParametro":"actividad",
"recomendacionParametro": "recomendacion",
"tipoAnalisisParam": "tipoAnalisis",
"tipoPlanParam": "tipoPlan"
}


def postAsociacion(data):
    try:
        entidadIntermedia = data.get('entidadIntermedia')
        codNomenclador = data.get('cod') #actividad, recomendación, tipoAnalisis, tipoPlan
        isActiv= True
        parametroJson = data.get ('parametros')
        parametrosList = parametroJson.get('cod')
        codParametroList = json.loads(parametrosList)

        if len(codParametroList)==0:
            raise Exception('N','la lista de parametros esta vacia')

        nomencladorObj = getNomencladoCod(nomenclador[entidadIntermedia],codNomenclador) 

        ##por cada parametro
        for  codParam in codParametroList:
            param = getNomencladoCod('parametro',codParam)
            asociacion = modelos[entidadIntermedia](isActiv = isActiv)
            asociacion.parametro = param #asocio el parametro
            
            ##asocio el nomenclador que puede ser actividad, recomendación, tipoAnalisis, tipoPlan
            if entidadIntermedia == 'actividadParametro':
                asociacion.actividad = nomencladorObj
            else:
                if entidadIntermedia =='recomendacionParametro':
                    asociacion.recomendacion = nomencladorObj
                else:
                    if entidadIntermedia == 'tipoAnalisisParam':
                        asociacion.tipoAnalisis = nomencladorObj
                    else:
                        if entidadIntermedia == 'tipoPlanParam':
                            asociacion.tipoPlan = nomencladorObj
            
            saveEntidadSinCommit(asociacion)
    
        Commit()
        return ResponseOk()
    except Exception as e:
        Rollback()
        return ResponseException(e)


def getAsociacionCod(entidadIntermedia,codNomenclador):
    try:
        ##recupero las clases intermedias 
        nomencladorObj = getNomencladoCod(nomenclador[entidadIntermedia],codNomenclador)
        paramList = getParamList(entidadIntermedia,nomencladorObj)

        dtoParamList = []
        for param in paramList:
            if param.isActiv: #filtro por activas
                dtoAuxParam = dict(codParametro = param.parametro.cod, nombreParametro =param.parametro.nombre, isActiv = param.parametro.isActiv)
                dtoParamList.append(dtoAuxParam)

        return (dict(parametros=dtoParamList))
    except Exception as e:
        return ResponseException(e)



def putAsociacion(data,entidadIntermedia,codNomenclador):
    try:    
        parametrosIngr = data.get('parametros') 
        paramListIngr = [] #lista de cod parametros ingresados
        isUpdate=False

        for p in parametrosIngr:
            cod = p.get('codParametro')
            paramListIngr.append(cod)

        nomencladorObj = getNomencladoCod(nomenclador[entidadIntermedia],codNomenclador)
        paramListObj = getParamList(entidadIntermedia,nomencladorObj)

        ##parametros ya existentes en la base de datos
        for param in paramListObj:
            codParam = param.parametro.cod
            if codParam in paramListIngr: #si el param de la db esta en la lista
                paramListIngr.remove(codParam)

                #si es false lo activo
                if not param.isActiv: 
                    isUpdate=True  
                    param.isActiv=True
                
            else:#si no esta en la lista lo desactivo
                #si es true lo desactivo y si es falso lo dejo 
                if param.isActiv:
                    isUpdate=True  
                    param.isActiv=False

            if isUpdate:
                saveEntidadSinCommit(param) 

        ## parametros nuevos que se deben agregar
        for codParamNew in paramListIngr:
            parametroNew = getNomencladoCod('parametro',codParamNew)
            asociacionNew = modelos[entidadIntermedia](isActiv=True)
            asociacionNew.parametro = parametroNew
            paramListObj.append(asociacionNew) 
    
        Commit()
        return ResponseOk()
    except Exception as e:
        Rollback()
        return ResponseException(e)


def getAsociaciones(entidadIntermedia):
    helperEntidad= {
        "actividadParametro":hlmodel.Actividad,
        "recomendacionParametro": hlmodel.Recomendacion,
        "tipoAnalisisParam": hlmodel.TipoAnalisis,
        "tipoPlanParam": hlmodel.TipoPlan
    }
    try:
        dtoAsociacionesList = []
        dtoSinAsociacionesList = []
        entidadList = selectAllisActiv(helperEntidad[entidadIntermedia])

        for entidad in entidadList:
            dtoAux = dict(cod=entidad.cod,nombre=entidad.nombre)
            cantidad = cantAsociaciones(entidad,entidadIntermedia)

            if cantidad > 0: ##tiene asociaciones
                dtoAsociacionesList.append(dtoAux)
            else:
                dtoSinAsociacionesList.append(dtoAux)

        return (dict(asociaciones=dtoAsociacionesList,sinAsociaciones=dtoSinAsociacionesList))
    except Exception as e:
        return ResponseException(e)



def getParamList(entidadIntermedia,nomencladorObj):
    if entidadIntermedia == 'actividadParametro':
            paramList = nomencladorObj.actividadParamList
    else:
        if entidadIntermedia =='recomendacionParametro':
                paramList = nomencladorObj.recomendacionParamList
        else:
            if entidadIntermedia == 'tipoAnalisisParam':
                    paramList = nomencladorObj.tipoAnalisisParamList
            else:
                if entidadIntermedia == 'tipoPlanParam':
                    paramList = nomencladorObj.tipoPlanParamList

    return paramList