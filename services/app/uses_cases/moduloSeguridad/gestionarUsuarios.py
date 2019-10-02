from flask import jsonify
from app.model import hlmodel
from app.repositorio.hlDb import saveEntidadSinCommit, selectByCod,Commit
from app.api.helperApi.hlResponse import ResponseException, ResponseOk
from app.shared.toLowerCase import toLowerCaseSingle, obtainDict
import json

modelos = {
"rol":hlmodel.Rol,
"usuario":hlmodel.Usuario,
}

def postUser(data):

    usuarioJson = data.get('usuario')
    rolJson = data.get('rol')
    #Buscar rol seleccionado
    rolRstList = selectByCod(hlmodel.Rol, rolJson.get('cod'))
    #Crear usuario
    usuario = hlmodel.Usuario.from_json(usuarioJson)
    usuario.rol = rolRstList
    saveEntidadSinCommit(usuario)

    Commit()

    return 'ok'