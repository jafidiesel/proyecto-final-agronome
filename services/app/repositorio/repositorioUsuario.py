from app.extensions import db
from app.repositorio.hlDb import Commit, saveEntidadSinCommit, Rollback
from app.model.hlmodel import Usuario, Rol
from app.uses_cases.moduloConfiguracion.gestionarNomenclador import getNomencladoCod
from app.api.helperApi.hlResponse import ResponseException, ResponseOk

def updateUser(usuarioJson, rolRst, cod):
    try:
        #Se busca el usuario, en caso de existir se actualiza el mismo
        usuarioRst = Usuario.query.filter(Usuario.cod == cod).one()
        #user = Usuario.from_json(usuarioJson)
        #Actualizar datos propios de Usuario
        usuarioRst.nombre = usuarioJson.get('nombre')
        usuarioRst.apellido = usuarioJson.get('apellido')
        usuarioRst.contraseniaUsuario =usuarioJson.get('contraseniaUsuario')
        usuarioRst.email = usuarioJson.get('email')
        usuarioRst.usuario = usuarioJson.get('usuario')
        usuarioRst.isActiv = usuarioJson.get('isActiv')
        #Actualizar Rol
        usuarioRst.rol = rolRst
        Commit()
        return ResponseOk()   
    except Exception as e:
        Rollback()
        return ResponseException(e)

def getUsuarioByName(nombre):
    try:
        usuario = Usuario.query.filter(Usuario.usuario == nombre).one()
        return usuario
    except Exception as e:
        return ResponseException(e)