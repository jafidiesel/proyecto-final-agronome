from app.extensions import db
from app.repositorio.hlDb import Commit, saveEntidadSinCommit, Rollback
from app.model.hlmodel import Usuario, Rol
from app.uses_cases.moduloConfiguracion.gestionarNomenclador import getNomencladoCod
from app.api.helperApi.hlResponse import ResponseException, ResponseOk

def updateUser(usuarioJson, rolRst):
    try:
        #Se busca el usuario, en caso de existir se actualiza el mismo
        usuarioRst = Usuario.query.filter(Usuario.cod == usuarioJson.get('cod')).one()
        user = Usuario.from_json(usuarioJson)
        #Actualizar datos propios de Usuario
        usuarioRst.nombre = user.nombre
        usuarioRst.apellido = user.apellido
        usuarioRst.email = user.email
        usuarioRst.usuario = user.usuario
        usuarioRst.isActiv = user.isActiv
        #Actualizar Rol
        usuarioRst.rol = rolRst
        Commit()
        return ResponseOk()   
    except Exception as e:
        Rollback()
        return ResponseException(e)

def getUsuarioByName(nombre):
    try:
        usuario = Usuario.query.filter(Usuario.nombre == nombre).one()
        return usuario
    except Exception as e:
        return ResponseException(e)