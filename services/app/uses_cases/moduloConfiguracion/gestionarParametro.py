from app.api.helperApi.hlDb import saveEntidad,selectAll2, selectAllByFilter
from flask import jsonify
from app.model.hlmodel import Parametro, ParametroOpcion, TipoParametro, TipoDato, Opcion
from app.uses_cases.moduloConfiguracion.gestionarNomenclador import getNomencladoCod

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
        #Buscar instancias a asociar

        tipoParametroRst = getNomencladoCod('tipoParametro', tipoParametroJson.get('id'))
        tipoDatoRst = getNomencladoCod('tipoDato', tipoDatoJson.get('id'))
        opcionRst = getNomencladoCod('opcion',opcionJson.get('id'))
      
        
        #Creacion  y asociación de Parametro 
        parametroRst = Parametro.from_json(parametroJson)     
        tipoDatoRst.parametroRef.append(parametroRst)
        tipoParametroRst.parametroRef.append(parametroRst)

        parametroOpcion = ParametroOpcion(True,parametroRst,opcionRst) #parametro opcion son muchos ojo

        parmNew =saveEntidad(parametroRst)
        
        #Creacion  y persistencia de ParametroOpcion 
        saveEntidad(parametroOpcion)
        return jsonify(parmNew.to_json())  
    except Exception as e:
        return str(e.__cause__)

def getParametro():
    return True
#en algun lado debe decri que nomenclador lo llama para poder filtrar por tipo
#EJ: si lo llama actividad, solo debe mostrar los parametros que son de tipo Actividad
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
    
