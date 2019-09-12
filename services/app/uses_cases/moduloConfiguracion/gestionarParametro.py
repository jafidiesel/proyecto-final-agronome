from app.api.helperApi.hlDb import saveEntidad,selectAll2, selectAllByFilter
from app.model.hlmodel import Parametro, ParametroOpcion, TipoParametro, TipoDato, Opcion
import json
from app.uses_cases.moduloConfiguracion.gestionarNomenclador import getNomencladoCod2
from app.extensions import db

def postParametro(data): 
    try:
        #Manejo de Json
        parametroJson = data.get('parametro')
        print(parametroJson)
        tipoParametroJson = data.get('tipoParametro')
        tipoDatoJson = data.get('tipoDato')
        opcionJson = data.get('opcion')

        
        #Buscar a asociar
        tipoParametroRst = getNomencladoCod2(tipoParametroJson, tipoParametroJson.get('id'))
        tipoDatoRst = getNomencladoCod2(tipoDatoJson, tipoDatoJson.get('id'))
        opcionRst = getNomencladoCod2(opcionJson,opcionJson.get('id'))
        #Verificar que las clases esten activas
        
        #Creacion  y persistencia de Parametro 

        parametroRst = Parametro.from_json(parametroJson)     
        tipoDatoRst.parametroRef.append(parametroRst)
        tipoParametroRst.parametroRef.append(parametroRst)
        ParametroOpcion(True,parametroRst,opcionRst) 
        
        saveEntidad(parametroRst)
        print("Despues de append")
      
        return Ok 
    except:
        
        return ("mala sintaxis")

def putParametro(data):
    return True

#Obtener todos los parametros con sus asociaciones TipoParametro y TipoDato. Retorna Json
def getParametros():
    for obj in selectAll2(Parametro):
        print(obj.nombre)
        print(obj.to_json())
        print(obj.to_json())

    return True

def getParametro():
    return True

#Listar atributos para combo: TipoDato, TipoParametro, Opcion
#https://es.stackoverflow.com/questions/24320/necesito-pasarle-dinamicamente-al-objeto-query-de-sqlalchemy-los-parametros-de/24748
def listarAtributos():
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