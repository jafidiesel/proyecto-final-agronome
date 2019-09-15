from flask import jsonify
from app.repositorio.hlDb import saveEntidad, saveEntidadSinCommit, Commit,Rollback ,selectAll
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
        codNomenclador = data.get('id') #actividad, recomendación, tipoAnalisis, tipoPlan
        isActiv= True
        parametroJson = data.get ('parametros')
        parametrosList = parametroJson.get('id')
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


def getEntidadIntermCod(entidadIntermedia,id):
    try:
        isFilterParam = False # no filtro por parametro
        objetos = selectByCodEspec(modelos[entidadIntermedia],entidadIntermedia,id,isFilterParam,'')
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


def putEntidadInterm(data,entidadIntermedia,id):
    try:
        isFilterParam = True
        codParam= data.get('idParametro')
        isActiv = data.get('isActiv')
        updateEntidadInterm(isActiv,modelos[entidadIntermedia],entidadIntermedia,id,isFilterParam,codParam) 
        return ResponseOk()
    except Exception as e:
        return ResponseException(e)







##SOLO SE DEJA DE EJEMPLO NO SE USA EN LA APIII PORQUE BUSCA TODO DE TODOS
def getEntidadInterm(entidadIntermedia):
    try:
        objetos = selectAll(modelos[entidadIntermedia])
        dtoParamList = []

        for obj in objetos:
            codParam = obj.codParametro
            param = getNomencladoCod('parametro',codParam)
            nombreParam = param.nombre

            entidad=nomenclador[entidadIntermedia]
            
            if entidad=='actividad':
                codNomen = obj.codActividad
                codDtoAux= 'codActividad'
                nomDtoAux= 'nombreActividad'
            else:
                if entidad=='recomendacion':
                    codNomen = obj.codRecomendacion
                    codDtoAux= 'codRecomendacion'
                    nomDtoAux= 'nombreRecomendacion'
                else:
                    if entidad=='tipoPlan':
                        codNomen = obj.codTipoPlan
                        codDtoAux= 'codTipoPlan'
                        nomDtoAux= 'nombreTipoPlan'
                    else:
                        if entidad=='tipoAnalisis':
                            codNomen = obj.codTipoAnalisis
                            codDtoAux= 'codTipoAnalisis'
                            nomDtoAux= 'nombreTipoAnalisis'
                        else:
                            raise Exception('N','error en la entidad')
        
            nomen = getNomencladoCod(entidad,codNomen)
            nombreNomen = nomen.nombre

            #definicion de un diccionario
            dtoAux =dict(isActiv=obj.isActiv,codParametro = obj.codParametro, nombreParametro= nombreParam)
            
            #se le agregan al diccionario estos campos al dic
            dtoAux[codDtoAux] = codNomen
            dtoAux[nomDtoAux] = nombreNomen
            
            dtoParamList.append(dtoAux)
        #endfor
            
        return (dict(parametro=dtoParamList))
        #return (json.dumps(dtoParamList))
    except Exception as e:
        return ResponseException(e)