from flask import jsonify,make_response
from app.model import hlmodel
from app.repositorio.hlDb import saveEntidadSinCommit, selectByCod,Commit, selectAll, Rollback
from app.api.helperApi.hlResponse import ResponseException, ResponseOk
from app.shared.toLowerCase import toLowerCaseSingle, obtainDict
import json
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app.shared.toLowerCase import toLowerCaseSingle, obtainDict
from app.uses_cases.moduloConfiguracion.gestionarNomenclador import getNomencladoCod

modelos = {
"rol":hlmodel.Rol,
"usuario":hlmodel.Usuario,
}

def postUser(data):
    try:
        dataLower = obtainDict(data)
        usuarioJson = dataLower.get('usuario')
        rolJson = dataLower.get('rol')
        print(rolJson)
        #Buscar rol seleccionado
        rolRst = selectByCod(hlmodel.Rol, rolJson.get('cod'))
        fincaListJson =  dataLower.get('finca')
        #Setear pws con hash
        #hashed_password = generate_password_hash(dataLower.get('contraseniaUsuario'), method = 'sha256')
        #Crear usuario
        usuario = hlmodel.Usuario.from_json(usuarioJson)
        usuario.contraseniaUsuario = usuarioJson.get('contraseniaUsuario')
        #Generar codPublic
        usuario.cod = str(uuid.uuid4())
        #Asociar Finca
        #Verificar tipo de rol asociado para asociar o no, la Finca correspondiente
        if ((rolRst.nombre == 'supervisor') or (rolRst.nombre == 'ingeniero')):
            print('En roles')
            #Si la lista de finca essta vacia, msj de error
            print(fincaListJson)
            if not fincaListJson:
                print('en finca vacio')
                return make_response(jsonify({'message:':'El usuario debe estar asociado a una Finca'}),404)

            listFincaRst = dataLower.get('finca')
            for finca in listFincaRst:
                #Buscar finca para verificar que existe,crear intermedia FincaUsuario y asociarla al usuario
                from app.repositorio.repositorioGestionarFinca import selectFincaCod
                fincaRst = selectFincaCod(finca.get('codFinca'))
                #Crear FincaUsario
                fincaUsuario = hlmodel.FincaUsuario()
                fincaUsuario.isActiv = True
                #Asociar Finca a ficnaUsuario
                fincaUsuario.finca = fincaRst
                #Asociar usuario a fincaUsuario
                usuario.fincaUsuarioList.append(fincaUsuario)            
                
        #Asociar rol
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
                #import pdb; pdb.set_trace()
                #Armado de diccionario
                usuarioDto = usuarioRst.toJson()
                usuariosList.append(usuarioDto)           
        return usuariosList
    except Exception as e:
        return ResponseException(e)

#Listar un Usuario
def getUsuario(codPublic):
    try:
        usuarioRst = selectByCod(hlmodel.Usuario, codPublic)        
        return usuarioRst.toJson()
    except Exception as e:
        return ResponseException(e)

#Editar Usuario
def updateUsuario(data, cod):
    dataLower = obtainDict(data)
    #Buscar usuario 
    usuarioJson = dataLower.get('usuario')
    #Modificaciones por parte del Admin
    claves = list(dataLower.keys())
    #Buscar Rol
    rolJson = dataLower.get('rol')  
    rolRst = getNomencladoCod(claves[1], rolJson.get('cod'))
    #Verificar tipo de rol asociado para asociar o no, la Finca correspondiente
    listFincaRst = dataLower.get('finca')         
    from app.repositorio.repositorioUsuario import updateUser
    return updateUser(usuarioJson, rolRst, cod, listFincaRst)        



    