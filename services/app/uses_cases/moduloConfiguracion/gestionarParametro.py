from flask import jsonify
from app.repositorio.hlDb import saveEntidad, saveEntidadSinCommit,Rollback,Commit,selectByCod, addObject, selectAll
from app.model.hlmodel import Parametro, ParametroOpcion, TipoParametro, TipoDato, Opcion
from app.uses_cases.moduloConfiguracion.gestionarNomenclador import getNomencladoCod
from app.api.helperApi.hlResponse import ResponseException, ResponseOk
import json
from app.repositorio.repositorioParametro import selectAllByParamCod,selectActiveByName,selectByValue,selectAllActiveByParamCod
from app.model import hlmodel

modelos = {
"tipoParametro": hlmodel.TipoParametro,
}

def postParametro(data): 
    try:
        #Manejo de Json
        parametroJson = data.get('parametro')
        tipoParametroJson = data.get('tipoParametro')
        tipoDatoJson = data.get('tipoDato')
        opcionJsonList = data.get('opcion')
        #Lista de claves del Json --> Para obenter el tipo de entidad
        claves = list(data.keys())

        #Busqueda de entidades a asociar a Parametro
        tipoParametroRst = getNomencladoCod(claves[1], tipoParametroJson.get('id'))
        tipoDatoRst = getNomencladoCod(claves[2], tipoDatoJson.get('id'))

        codOpcionList=[]
        for opcionJson in opcionJsonList:
            codOpcionList.append(opcionJson.get('id'))
              
        #Creacion  y asociación de Parametro 
        parametroRst = Parametro.from_json(parametroJson) 
        addObject(parametroRst)
        tipoParametroRst.parametroTipo.append(parametroRst)
        tipoDatoRst.parametroDato.append(parametroRst)

        #Creacion  y asociación de OpcionParametro 
        codParametro = parametroRst.cod
        for cod in codOpcionList:
            parametroOpcion = ParametroOpcion(True,codParametro,cod) 
            saveEntidadSinCommit(parametroOpcion)           
        
        Commit() 
        return ResponseOk()
    except Exception as e:
        Rollback()
        return ResponseException(e)

def getParametro():
    return True

#Para el armado de las estructuras
def getParametroEstructura(entidad):
    try:        
        #Buscar TipoParametro por nombre: 
        tipoParametroRst = selectActiveByName(modelos['tipoParametro'],entidad)
        if not tipoParametroRst:
            raise Exception('N','No existe el codigo ingresado')
        #Obtension de Parametros asociados a TipoParametro
        parametroRstList = selectByValue(hlmodel.Parametro,tipoParametroRst.cod)
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
            #dtoParametro.append(dict(parametro = parametroDto))
            dtoParametro.append(parametroDto)
        return jsonify(dtoParametro)
    except Exception as e:
        Rollback()
        return ResponseException(e)

            
def getParametroById(id):  
    try:
        dtoGeneral= []
        dtoOpcionList = []

        parametro = selectByCod(hlmodel.Parametro,id)
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
        tipoDatoDto.pop('_sa_instance_state',None)
        tipoParametroDto.pop('_sa_instance_state',None)
        
        #Busqueda por ID de entidades Opcion relacionadas a parametroOpcion
        for parametroOp in selectAllByParamCod(parametro.cod):
                opcion =selectByCod(hlmodel.Opcion,parametroOp.codOpcion)
                opcionDto = opcion.__dict__
                opcionDto.pop('_sa_instance_state',None)
                dtoOpcionList.append(opcionDto)
        
        dtoGeneral.append(dict(parametro = parametroDto,tipoParametro = tipoParametroDto,tipoDato = tipoDatoDto,opcion=dtoOpcionList))
        return jsonify(dtoGeneral)
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
            dtoParametro.append(parametroDto)
        return jsonify(dtoParametro)
    except Exception as e:
        Rollback()
        return ResponseException(e)
        
def updateParametro(data):
    
        #Extraccion de datos    
        parametroJson = data.get('parametro')
        tipoParametroJson = data.get('tipoParametro')
        tipoDatoJson = data.get('tipoDato')
        opcionJsonList = data.get('opcion')
        #Lista de claves del Json --> Para obtener el tipo de entidad
        claves = list(data.keys())
        #Busqueda de entidades a asociar a Parametro
        tipoParametroRst = getNomencladoCod(claves[1], tipoParametroJson.get('id'))
        tipoDatoRst = getNomencladoCod(claves[2], tipoDatoJson.get('id'))

        from app.repositorio.repositorioParametro import updateParam

        updateParam(parametroJson,tipoParametroRst,tipoDatoRst,opcionJsonList)
        return "Hello"
    