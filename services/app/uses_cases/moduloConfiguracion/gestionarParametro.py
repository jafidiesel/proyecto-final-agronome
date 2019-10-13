from flask import jsonify
from app.repositorio.hlDb import saveEntidad, saveEntidadSinCommit,Rollback,Commit,selectByCod, addObject, selectAll
from app.model.hlmodel import Parametro, ParametroOpcion, TipoParametro, TipoDato, Opcion
from app.uses_cases.moduloConfiguracion.gestionarNomenclador import getNomencladoCod
from app.api.helperApi.hlResponse import ResponseException, ResponseOk
import json
from app.repositorio.repositorioParametro import selectAllByParamCod,selectActiveByName,selectByValue,selectAllActiveByParamCod
from app.model import hlmodel
from app.shared.toLowerCase import toLowerCaseSingle, obtainDict

modelos = {
"actividad":hlmodel.Actividad,
"estadoPlanificacion":hlmodel.EstadoPlanificacion,
"opcion":hlmodel.Opcion,
"permiso": hlmodel.Permiso,
"recomendacion": hlmodel.Recomendacion,
"recurso": hlmodel.Recurso,
"rol": hlmodel.Rol,
"tipoAnalisis": hlmodel.TipoAnalisis,
"tipoCultivo": hlmodel.TipoCultivo,
"tipoDato": hlmodel.TipoDato,
"tipoParametro": hlmodel.TipoParametro,
"tipoPlan": hlmodel.TipoPlan,
"tipoPlanificacion": hlmodel.TipoPlanificacion,
"tipoRecurso": hlmodel.TipoRecurso,
"parametro": hlmodel.Parametro #agregue esto para usarlo en gestionar entidad intermedia, darle una vuelta de rosca mas con la chechi, basicamente el parametro no es un nomenclador comun, pero lo necesito aca para reutilizar la funcion getNomencladorCod
}

def postParametro(data): 
    try:
        #Manejo de Json
        dataLower = obtainDict(data)
        parametroJson = dataLower.get('parametro')
        tipoParametroJson = dataLower.get('tipoParametro')
        tipoDatoJson = dataLower.get('tipoDato')
        opcionJsonList = dataLower.get('opcion')
        #Lista de claves del Json --> Para obenter el tipo de entidad
        claves = list(dataLower.keys())

        #Busqueda de entidades a asociar a Parametro
        tipoParametroRst = getNomencladoCod(claves[1], tipoParametroJson.get('cod'))
        tipoDatoRst = getNomencladoCod(claves[2], tipoDatoJson.get('cod'))

        codOpcionList=[]
        for opcionJson in opcionJsonList:
            codOpcionList.append(opcionJson.get('cod'))
              
        #Creacion  y asociación de Parametro 
        parametroRst = Parametro.from_json(parametroJson) 
        addObject(parametroRst)
        tipoParametroRst.parametroTipo.append(parametroRst)
        tipoDatoRst.parametroDato.append(parametroRst)

        #Relacion intermedia: ParametroOpcion
        #First: Crear el Padre de la relacion: Parametro
        #Second: Crear la intermedia con los datos adicionales
        #Third: Crear el hijo y asociarlo a la intermedia
        #Fourth: Asociar la intermedia al padre
        for opcionJson in opcionJsonList:
            parametroOpcion = ParametroOpcion(True)
            opcionRst = getNomencladoCod(claves[3], opcionJson.get('cod'))
            parametroOpcion.opcion = opcionRst
            parametroRst.paramOpcion.append(parametroOpcion) 
        
        Commit() 
        return ResponseOk()
    except Exception as e:
        Rollback()
        return ResponseException(e)

#Para el armado de las estructuras
def getParametroEstructura(entidad):
    try:        
        #Buscar TipoParametro por nombre: 
        tipoParametroRst = selectActiveByName(modelos['tipoParametro'],entidad)
        if not tipoParametroRst:
            raise Exception('N','No existe el codigo ingresado')
        #Obtension de Parametros asociados a TipoParametro
        parametroRstList = tipoParametroRst.parametroTipo
        if not parametroRstList:
            raise Exception('N','No existen parametros asociados')
        dtoParametro = []
        #Obtener TipoDato activo y las opciones de cada parametro
        for parametro in parametroRstList:        
            parametroDto = parametro.__dict__            
            parametroDto.pop('_sa_instance_state',None)
            parametroDto.pop('codTipoParametro', None)
            parametroDto.pop('codTipoDato', None)
            parametroDto.pop('tipoParametroRef', None)
            parametroDto.pop('tipoDatoRef', None)
            dtoParametro.append(parametroDto)
        return jsonify(dtoParametro)
    except Exception as e:
        Rollback()
        return ResponseException(e)

            
def getParametroById(cod):  
    try:
        dtoGeneral= []
        dtoOpcionList = []
        parametro = selectByCod(hlmodel.Parametro,cod)        
        #Busqueda por ID de entidades Opcion relacionadas a parametroOpcion
        for parametroOp in parametro.paramOpcion:
                #opcion =selectByCod(hlmodel.Opcion,parametroOp.codOpcion)
                if (parametroOp.isActiv == True):
                    opcionRst = parametroOp.opcion
                    if (opcionRst.isActiv == True):
                        opcionDto = opcionRst.__dict__
                        opcionDto.pop('_sa_instance_state',None)
                        dtoOpcionList.append(opcionDto)
        #Creacion dto parametro
        parametroDto = parametro.__dict__
        #Creacion dto tipoParametro
        tipoParametroDto = parametro.tipoParametroRef.__dict__
        #Creacion dto tipoDato
        tipoDatoDto = parametro.tipoDatoRef.__dict__
        ##Eliminacion de datos innecesarios de los diccionarios
        parametroDto.pop('_sa_instance_state',None)
        parametroDto.pop('codTipoParametro', None)
        parametroDto.pop('codTipoDato', None)
        parametroDto.pop('tipoParametroRef', None)
        parametroDto.pop('tipoDatoRef', None)
        parametroDto.pop('paramOpcion', None)
        tipoDatoDto.pop('_sa_instance_state',None)
        tipoParametroDto.pop('_sa_instance_state',None)
        
        #return jsonify(dict(parametro = parametroDto,tipoParametro = tipoParametroDto,tipoDato = tipoDatoDto,opcion=dtoOpcionList))
        return (dict(parametro = parametroDto,tipoParametro = tipoParametroDto,tipoDato = tipoDatoDto,opcion=dtoOpcionList))
    except Exception as e:
        Rollback()
        return ResponseException(e)

def getAllParametros():
    #Buscar todos los parametros Activos e Inactivos 
    try:
        parametroRstList = selectAll(hlmodel.Parametro)
        dtoParametro = []
        #Obtener TipoDato activo y las opciones de cada parametro
        for parametro in parametroRstList:        
            parametroDto = parametro.__dict__            
            parametroDto.pop('_sa_instance_state',None)
            parametroDto.pop('codTipoParametro', None)
            parametroDto.pop('codTipoDato', None)
            parametroDto.pop('tipoParametroRef', None)
            parametroDto.pop('tipoDatoRef', None)
            parametroDto.pop('paramOpcion', None)
            dtoParametro.append(parametroDto)
        return jsonify(dtoParametro)
    except Exception as e:
        Rollback()
        return ResponseException(e)
        
def updateParametro(data):
    
    dataLower = obtainDict(data)
    print(dataLower)
    #Extraccion de datos    
    parametroJson = dataLower.get('parametro')
    tipoParametroJson = dataLower.get('tipoParametro')
    tipoDatoJson = dataLower.get('tipoDato')
    opcionJsonList = dataLower.get('opcion')
    #Lista de claves del Json --> Para obtener el tipo de entidad
    claves = list(dataLower.keys())
    #Busqueda de entidades a asociar a Parametro
    tipoParametroRst = getNomencladoCod(claves[1], tipoParametroJson.get('cod'))
    tipoDatoRst = getNomencladoCod(claves[2], tipoDatoJson.get('cod'))
    from app.repositorio.repositorioParametro import updateParam        
    return updateParam(parametroJson,tipoParametroRst,tipoDatoRst,opcionJsonList)
   

    