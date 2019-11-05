from flask import jsonify,make_response
from app.model import hlmodel
from app.repositorio.hlDb import saveEntidadSinCommit, selectByCod,Commit, selectAll, Rollback
from app.api.helperApi.hlResponse import ResponseException, ResponseOk,ResponseOkmsg
from app.shared.toLowerCase import toLowerCaseSingle, obtainDict
import json
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app.shared.toLowerCase import toLowerCaseSingle, obtainDict
from app.uses_cases.moduloConfiguracion.gestionarNomenclador import getNomencladoCod
from app.repositorio.repositorioGestionarFinca import selectFincaCod
from app.repositorio.repositorioUsuario import updateUser,selectAllUser, getUsuarioByName
from flask_mail import Mail, Message
import jwt

modelos = {
"rol":hlmodel.Rol,
"usuario":hlmodel.Usuario,
}

def postUser(data):
    #try:
    dataLower = obtainDict(data)
    usuarioJson = dataLower.get('usuario')
    rolJson = dataLower.get('rol')
    #print(rolJson)
    #Buscar rol seleccionado
    rolRst = selectByCod(hlmodel.Rol, rolJson.get('cod'))
    #print(rolRst)
    fincaListJson =  dataLower.get('finca')
    #print(fincaListJson)
    #Setear pws con hash
    #hashed_password = generate_password_hash(dataLower.get('contraseniaUsuario'), method = 'sha256')
    #Crear usuario
    usuario = hlmodel.Usuario.from_json(usuarioJson)
    usuario.contraseniaUsuario = usuarioJson.get('contraseniaUsuario')
    #Generar codPublic
    codUUID = str(uuid.uuid4())
    usuario.cod = codUUID
    #Asociar Finca
    #Verificar tipo de rol asociado para asociar o no, la Finca correspondiente
    
    if False: #((rolRst.nombre == 'supervisor') or (rolRst.nombre == 'ingeniero')):
        #Si la lista de finca essta vacia, msj de error
        if not fincaListJson:
            return make_response(jsonify({'message:':'El usuario debe estar asociado a una Finca'}),404)

        listFincaRst = dataLower.get('finca')
        for finca in listFincaRst:
            #Buscar finca para verificar que existe,crear intermedia FincaUsuario y asociarla al usuario
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

    #Setiar flag de account 
    usuario.isRecuperarContrasenia = False
    usuario.isActiv = False
    token = str(usuario.getToken())
    saveEntidadSinCommit(usuario)
    Commit()
    token = token.replace("b'",'')

    from app.backend import app
    #print(app.config.get('MAIL_USERNAME'))
    with app.app_context():
    
        mail = Mail(app)
        msg = Message('Activación de cuenta - Agronome', sender = app.config.get('MAIL_USERNAME'), recipients = [usuario.email])
        texto = 'Bienvenido a Agronome {} \nSus datos de registro son: \n\t -Usuario: {}\n\t -Contraseña: {}\nPara activar su cuenta utilice el siguiente enlace:'.format(usuario.usuario, usuario.usuario, usuario.contraseniaUsuario)
        url = 'http://localhost:4200/activar/' + str(token)
        texto = texto +  '\n' + url
        msg.body = texto
        mail.send(msg)
    
    
    return ResponseOk()

#Listar usuarios. Mostrar 
def getAllUsers():
    try:
        usuariosList  = []
        usuarioRstList = selectAllUser()
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
    return updateUser(usuarioJson, rolRst, cod, listFincaRst)        



def activateUser(currentUser):
    try:
        if currentUser.isActiv:
            raise Exception('N', 'El usuario ' + currentUser.usuario +  ' ya se encuentra activo')
        else: 
            currentUser.isActiv = True
            saveEntidadSinCommit(currentUser)
            Commit()
        return ResponseOk()
    except Exception as e:
        return ResponseException(e)


def requestRecoverPass(data):
    try:
        user = data.get('usuario')
        usuario = getUsuarioByName(user)
        usuario.isRecuperarContrasenia = True
        token = str(usuario.getToken())
        saveEntidadSinCommit(usuario)
        Commit()
        token = token.replace("b'",'')

        from app.backend import app
        #print(app.config.get('MAIL_USERNAME'))
        with app.app_context():
        
            mail = Mail(app)
            msg = Message('Restablecer contraseña - Agronome', sender = app.config.get('MAIL_USERNAME'), recipients = [usuario.email])
            texto = 'Estimado {} \nPara restablecer contraseña utilice el siguiente enlace:'.format(usuario.usuario)
            url = 'http://localhost:4200/recuperar/' + str(token)
            texto = texto +  '\n' + url
            msg.body = texto
            mail.send(msg)
        return ResponseOkmsg('Por favor revisa tu correo electrónico')
    except Exception as e:
        return ResponseException(e)


def restorePass(data,currentUser):
    try:
        if not currentUser.isActiv:
            raise Exception('N','El usuario ' + currentUser.usuario + ' se encuentra desactivado')

        if not currentUser.isRecuperarContrasenia:
            raise Exception('N', 'No tenemos una solicitud para recuperar contraseña')
        
        
        passnew = data.get('contraseniaUsuario')    

        currentUser.isRecuperarContrasenia = False
        currentUser.contraseniaUsuario = passnew
        saveEntidadSinCommit(currentUser)
        Commit()
        return ResponseOk()
    except Exception as e:
        return ResponseException(e)