from flask import jsonify
from app.repositorio.hlDb import saveEntidad, saveEntidadSinCommit,Rollback,Commit,selectByCod, addObject
from app.model.hlmodel import Parametro, ParametroOpcion, TipoParametro, TipoDato, Opcion
from app.uses_cases.moduloConfiguracion.gestionarNomenclador import getNomencladoCod
from app.api.helperApi.hlResponse import ResponseException, ResponseOk
import json
from app.repositorio.repositorioParametro import selectAllByParamCod


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
        print(tipoDatoRst.cod)
        codOpcionList=[]
        for opcionJson in opcionJsonList:
            codOpcionList.append(opcionJson.get('id'))
            
        #Verificar que las clases esten activas
              
        #Creacion  y asociación de Parametro 
        parametroRst = Parametro.from_json(parametroJson) 
        addObject(parametroRst)
        tipoParametroRst.parametroTipo.append(parametroRst)
        tipoDatoRst.parametroDato.append(parametroRst)

        """parametroRst.tipoDatoRef.append(tipoDatoRst)
        print("Hola1")
        param.tipoParametroRef.append(tipoParametroRst)
        print("Hola2")
        tipoDatoRst.parametroRef.append(parametroRst)
        #tipoParametroRst.parametroRef.append(parametroRst)

        saveEntidadSinCommit(parametroRst)
        """
        #Creacion  y asociación de OpcionParametro 
        codParametro = parametroRst.cod
        for codOpcion in codOpcionList:
            parametroOpcion = ParametroOpcion(True,codParametro,codOpcion) 
            saveEntidadSinCommit(parametroOpcion)           
        
        Commit() 
        return ResponseOk()
    except Exception as e:
        Rollback()
        return ResponseException(e)

def getParametro():
    return True
#en algun lado debe decri que nomenclador lo llama para poder filtrar por tipo
#EJ: si lo llama actividad, solo debe mostrar los parametros que son de tipo Actividad
#Listar atributos para combo: TipoDato, TipoParametro, Opcion
#https://es.stackoverflow.com/questions/24320/necesito-pasarle-dinamicamente-al-objeto-query-de-sqlalchemy-los-parametros-de/24748
#Para el armado de las estructuras
def getParametroEstructura(tipoNomenclador):
    
    queryString={"isActiv" : 'isActiv'}
    #Buscar TipoParametro isActiv = True
    print("----------------")
    for obj in selectAllByFilter(TipoParametro,getattr(TipoParametro,queryString['isActiv']),True):
        print(obj.to_json())
    print("----------------")
    #Buscar TipoDato isActiv = True
    print("----------------")
    for obj in TipoDato.query.filter(TipoDato.isActiv == True).all():
        print(obj.to_json())
    print("----------------")
    #Buscar Opcions isActiv = True
    for obj in TipoDato.query.filter(TipoDato.isActiv == True).all():
        print(obj.to_json())
    print("----------------")
    return True
    
def getParametroById(id):  
    from app.model import hlmodel

    parametro = selectByCod(hlmodel.Parametro,id)
    for obj in ParametroOpcion.query.filter(ParametroOpcion.codParametro == parametro.cod).all():
        print(obj.to_json)
        print(obj.codParametro)


def updateParametro():
    return "Hello"