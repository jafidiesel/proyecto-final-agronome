<<<<<<< HEAD
from flask import jsonify
from app.api.helperApi.hlDb import saveEntidad
=======
from app.api.helperApi.hlDb import saveEntidad,selectAll2
>>>>>>> develop-backend
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

        #Buscar instancias a asociar

        tipoParametroRst = getNomencladoCod('tipoParametro', tipoParametroJson.get('id'))
        tipoDatoRst = getNomencladoCod('tipoDato', tipoDatoJson.get('id'))
        opcionRst = getNomencladoCod('opcion',opcionJson.get('id'))
      
        
        #Creacion  y asociación de Parametro 
        parametroRst = Parametro.from_json(parametroJson)     
        tipoDatoRst.parametroRef.append(parametroRst)
        tipoParametroRst.parametroRef.append(parametroRst)
<<<<<<< HEAD

        parametroOpcion = ParametroOpcion(True,parametroRst,opcionRst) #parametro opcion son muchos ojo

        parmNew =saveEntidad(parametroRst)
        
        #Creacion  y persistencia de ParametroOpcion 
        saveEntidad(parametroOpcion)
        return jsonify(parmNew.to_json())  
    except Exception as e:
        return str(e.__cause__)

    
=======
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
>>>>>>> develop-backend
