from app.extensions import db
from app.repositorio.hlDb import Commit, saveEntidadSinCommit, Rollback
from app.model.hlmodel import Usuario, Rol, FincaUsuario,Finca
from app.uses_cases.moduloConfiguracion.gestionarNomenclador import getNomencladoCod
from app.api.helperApi.hlResponse import ResponseException, ResponseOk
from sqlalchemy.orm import exc


def updateUser(usuarioJson, rolRst, cod, listFincaRst):
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
        #Actualizar Fincas
        #Verificar si las Fincas asociadas al usuario de la BD, son iguales o no, a las Fincas del Json
        #Si la Finca traida de la Bd no se encuentra en el Json, setear isActiv = False
        fincaUsuarioListRst = usuarioRst.fincaUsuarioList
        for fincaUsuarioRst in fincaUsuarioListRst:
            fincaRst = fincaUsuarioRst.finca
        Commit()
        return ResponseOk()   
    except Exception as e:
        Rollback()
        return ResponseException(e)

def getUsuarioByName(nombre):
    try:
        usuario = Usuario.query.filter(Usuario.usuario == nombre).one()
        return usuario
    except exc.NoResultFound:
        raise Exception('N', 'Usuario no encontrado')
    except Exception as e:
        return ResponseException(e)