from flask import jsonify
from app.model import hlmodel
from app.repositorio.hlDb import saveEntidadSinCommit, selectByCod,Commit, selectAll, Rollback
from app.api.helperApi.hlResponse import ResponseException, ResponseOk
from app.shared.toLowerCase import toLowerCaseSingle, obtainDict
import json
import uuid
from werkzeug.security import generate_password_hash, check_password_hash

modelos = {
"rol":hlmodel.Rol,
"usuario":hlmodel.Usuario,
}

def postUser(data):
    try:
        usuarioJson = data.get('usuario')
        rolJson = data.get('rol')
        #Buscar rol seleccionado
        rolRst = selectByCod(hlmodel.Rol, rolJson.get('cod'))
        #Setear pws con hash
        hashed_password = generate_password_hash(data.get('contraseniaUsuario'), method = 'sha256')
        #Crear usuario
        usuario = hlmodel.Usuario.from_json(usuarioJson)
        usuario.contraseniaUsuario = hashed_password
        #Generar codPublic
        usuario.codPublic = str(uuid.uuid4())
        usuario.rol = rolRst
        saveEntidadSinCommit(usuario)

        Commit()
        return ResponseOk()
    except Exception as e:
        Rollback()
        return ResponseException(e)

#Listar usuarios. Mostrar 
def getAllUsers():
    try:
        usuariosList  = []
        usuarioRstList = selectAll(hlmodel.Usuario)
        if not usuarioRstList:
            raise Exception('N','No existen Usuarios')
        else:
            for usuarioRst in usuarioRstList:
                print(usuarioRst.rol)
                #Armado de diccionario
                usuarioDto = usuarioRst.__dict__
                
                #Buscar Rol asociado a Usuario
                rolRst = usuarioRst.rol
                rolDto = rolRst.__dict__
                #Insertar rolDto
                usuarioDto['rol'] = rolDto
                #Eliminacion de datos innecesarios
                usuarioDto.pop('_sa_instance_state',None)
                usuarioDto.pop('randomContrasenia', None)
                usuarioDto.pop('isRecuperarContrasenia', None)
                usuarioDto.pop('cod', None)
                usuarioDto.pop('codRol', None)
                rolDto.pop('_sa_instance_state',None)
                rolDto.pop('tipoNomenclador', None)
                usuariosList.append(usuarioDto)
        return jsonify(usuariosList)
    except Exception as e:
        return ResponseException(e)
