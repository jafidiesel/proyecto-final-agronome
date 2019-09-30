from flask import jsonify
from app.repositorio.hlDb import saveEntidad, saveEntidadSinCommit, Commit,Rollback ,selectAll, selectByisActivAUX
from app.repositorio.DbEntidadIntermedia import selectByCodEspec, updateEntidadInterm
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


def postEntidadInterm(data):
    try:
        entidadIntermedia = data.get('entidadIntermedia')
        codNomenclador = data.get('cod') #actividad, recomendación, tipoAnalisis, tipoPlan
        isActiv= True
        parametroJson = data.get ('parametros')
        parametrosList = parametroJson.get('cod')
        codParametroList = json.loads(parametrosList)
        

        if len(codParametroList)==0:
            raise Exception('N','la lista de parametros esta vacia')


        #por cada parametro enviado
        for  idParam in codParametroList:
            intermedia = modelos[entidadIntermedia](isActiv,idParam,codNomenclador)
            saveEntidadSinCommit(intermedia)

        Commit()
        return ResponseOk()

    except Exception as e:
        Rollback()
        return ResponseException(e)


def getEntidadIntermCod(entidadIntermedia,cod):
    try:
        objetos = selectByCodEspec(modelos[entidadIntermedia],entidadIntermedia,cod)
        dtoParamList = []

        for obj in objetos:
            #print(obj)
            codParam = obj.codParametro
            param = getNomencladoCod('parametro',codParam)
            nombreParam = param.nombre

            dtoAux =dict(codParametro = obj.codParametro, nombreParametro= nombreParam, isActiv= obj.isActiv)
            dtoParamList.append(dtoAux)
        # #endfor
        return (dict(parametros=dtoParamList))
    except Exception as e:
        return ResponseException(e)


def putEntidadInterm(data,entidadIntermedia,cod):
    try:
        updateEntidadInterm(data,modelos[entidadIntermedia],entidadIntermedia,cod) 
        return ResponseOk()
    except Exception as e:
        return ResponseException(e)



def getEntidadInterm(entidadIntermedia):
    helperEntidad= {
        "actividadParametro":hlmodel.Actividad,
        "recomendacionParametro": hlmodel.Recomendacion,
        "tipoAnalisisParam": hlmodel.TipoAnalisis,
        "tipoPlanParam": hlmodel.TipoPlan
    }

    try:
        #objetos = selectAll(modelos[entidadIntermedia])
        objetos = selectByisActivAUX(modelos[entidadIntermedia],True)
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
            print(nomen.isActiv)
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