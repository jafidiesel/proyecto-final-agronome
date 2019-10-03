from flask import jsonify
from app.repositorio.hlDb import saveEntidad, saveEntidadSinCommit, Commit,Rollback ,selectAll
from app.repositorio.repositorioGestionarAsociacion import selectByCodEspec, updateEntidadInterm,selectByisActiv
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

nomenclador = { ##para detectar la entidad n de la entemedia ya que una es parametro y la otra es A/R/T/T
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
        ##recupero la clase intermedia segun el nomenclador
        nomencladorObj = getNomencladoCod(nomenclador[entidadIntermedia],codNomenclador) 
        if entidadIntermedia == 'actividadParametro':
                ParamList = nomencladorObj.actividadParamList
        else:
            if entidadIntermedia =='recomendacionParametro':
                    ParamList = nomencladorObj.recomendacionParamList
            else:
                if entidadIntermedia == 'tipoAnalisisParam':
                        ParamList = nomencladorObj.tipoAnalisisParamList
                else:
                    if entidadIntermedia == 'tipoPlanParam':
                        ParamList = nomencladorObj.tipoPlanParamList

        dtoParamList = []
        for param in ParamList:
            if param.isActiv: #filtro por activas
                dtoAuxParam = dict(codParametro = param.parametro.cod, nombreParametro =param.parametro.nombre, isActiv = param.parametro.isActiv)
                dtoParamList.append(dtoAuxParam)

        return (dict(parametros=dtoParamList))
    except Exception as e:
        return ResponseException(e)


def putAsociacion(data,entidadIntermedia,id):
    try:
        updateEntidadInterm(data,modelos[entidadIntermedia],entidadIntermedia,id) 
        return ResponseOk()
    except Exception as e:
        return ResponseException(e)



def getAsociaciones(entidadIntermedia):
    helperEntidad= {
        "actividadParametro":hlmodel.Actividad,
        "recomendacionParametro": hlmodel.Recomendacion,
        "tipoAnalisisParam": hlmodel.TipoAnalisis,
        "tipoPlanParam": hlmodel.TipoPlan
    }

    try:
        objetos = selectByisActiv(modelos[entidadIntermedia],True)
        entidades = selectAll(helperEntidad[entidadIntermedia])
        dtoAsociacionesList = []
        dtoSinAsociacionesList = []
        #print(entidades)
        for obj in objetos:
            entidad=nomenclador[entidadIntermedia]
            if entidad=='actividad':
                codNomen = obj.codActividad
            else:
                if entidad=='recomendacion':
                    codNomen = obj.codRecomendacion
                else:
                    if entidad=='tipoPlan':
                        codNomen = obj.codTipoPlan
                    else:
                        if entidad=='tipoAnalisis':
                            codNomen = obj.codTipoAnalisis
                        else:
                            raise Exception('N','error en la entidad')
        
            nomen = getNomencladoCod(entidad,codNomen)
            nombreNomen = nomen.nombre
            #print(nomen.isActiv)
            dtoAux = dict(cod=codNomen,nombre=nombreNomen)
            ##armo la lista con asociaciones
            if not dtoAux in dtoAsociacionesList:
                dtoAsociacionesList.append(dtoAux)
        #endfor

        #elimino de las entidades las que tienen asociaciones
        for item in dtoAsociacionesList:
            for ent in entidades:
                if  item['cod'] == ent.cod:
                    entidades.remove(ent)

        #transformo la entidades que no tienen asociaciones en dicc
        for dto in entidades:
            dtoAuxSin = dict(cod = dto.cod, nombre = dto.nombre)
            dtoSinAsociacionesList.append(dtoAuxSin)

        return (dict(asociaciones=dtoAsociacionesList,sinAsociaciones=dtoSinAsociacionesList))
    except Exception as e:
        return ResponseException(e)