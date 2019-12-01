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
from app.repositorio.repositorioUsuario import updateUser,selectAllUser, getUsuarioByName, getUsuarioByEmail, getUsuarioByUsuario
from flask_mail import Mail, Message
import jwt

modelos = {
"rol":hlmodel.Rol,
"usuario":hlmodel.Usuario,
}

#url para email 
urlFront = {
    'activate' : 'http://localhost:4200/activar/',
    'recoverPass' : 'http://localhost:4200/recuperar/' 
}

def postUser(data):
    try:
        dataLower = obtainDict(data)
        usuarioJson = dataLower.get('usuario')
        rolJson = dataLower.get('rol')
        rolRst = selectByCod(hlmodel.Rol, rolJson.get('cod'))
        fincaListJson =  dataLower.get('fincas')
        #Setear pws con hash
        #hashed_password = generate_password_hash(dataLower.get('contraseniaUsuario'), method = 'sha256')
        #Check usuario y email unique
        userUsuario = usuarioJson.get('usuario')
        email = usuarioJson.get('email')
        contraseniaUsuario = usuarioJson.get('contraseniaUsuario')
        #check
        hlCheckUsuario(userUsuario)
        hlCheckEmail(email)
        hlCheckPass(contraseniaUsuario) 

        #Crear usuario
        usuario = hlmodel.Usuario.from_json(usuarioJson)
        usuario.contraseniaUsuario = usuarioJson.get('contraseniaUsuario')
        #Generar codPublic
        codUUID = str(uuid.uuid4())
        usuario.cod = codUUID
        usuario.isRecuperarContrasenia = False
        usuario.isActiv = False

        #Asociar Finca 
        cantFinca = len(fincaListJson)
        print(str(cantFinca))

        #Verificar tipo de rol asociado para asociar o no, la Finca correspondiente
        if ((rolRst.nombre == 'supervisor') or (rolRst.nombre == 'ingeniero')):
            #Si la lista de finca essta vacia, msj de error
            if cantFinca == 0:
                raise Exception('N','El usuario debe estar asociado a una Finca')

            if (rolRst.nombre == 'supervisor') and cantFinca > 1:
                raise Exception('N','Un supervisor solo puede ser asignado a una finca')

            
            
            for finca in fincaListJson:
                #Buscar finca para verificar que existe,crear intermedia FincaUsuario y asociarla al usuario
                codFinca = finca.get('codFinca')
                fincaRst = selectFincaCod(codFinca)
                if not fincaRst:
                    raise Exception('N','No existe finca con cod: ' + str(codFinca))
                #Crear FincaUsario
                fincaUsuario = hlmodel.FincaUsuario()
                fincaUsuario.isActiv = True
                #Asociar Finca a ficnaUsuario
                fincaUsuario.finca = fincaRst
                #Asociar usuario a fincaUsuario
                usuario.fincaUsuarioList.append(fincaUsuario)            
                    
        #Asociar rol
        usuario.rol = rolRst

        token = str(usuario.getToken())
        saveEntidadSinCommit(usuario)
        Commit()
        token = hlformatToken(token)
        
        from app.shared.hlSendEmail import sendEmail
        key = 'activate'
        body = 'Bienvenido a Agronome {} \nSus datos de registro son: \n\t -Usuario: {}\n\t -Contraseña: {}\nPara activar su cuenta utilice el siguiente enlace:\n {}{}'.format(usuario.usuario, usuario.usuario, usuario.contraseniaUsuario,urlFront[key],token)
        html = ''
        additionals = []
        userList = []
        userList.append(usuario)
        msg = sendEmail(key,userList,body,html,additionals)

        return ResponseOkmsg(msg)
    except Exception as e:
        return ResponseException(e)
        

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
        return ResponseOkmsg('Su usuario fue activado exitosamente')
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
        token = hlformatToken(token)
        
        from app.shared.hlSendEmail import sendEmail
        key = 'recoverPass'
        body = 'Estimado '+ usuario.usuario+ '\nPara restablecer contraseña utilice el siguiente enlace:\n' + urlFront[key] + token 
        html = ''
        additionals = []
        userList = []
        userList.append(usuario)
        msg = sendEmail(key,userList,body,html,additionals)

        return ResponseOkmsg(msg)
    except Exception as e:
        return ResponseException(e)


def restorePass(data,currentUser):
    try:
        if not currentUser.isActiv:
            raise Exception('N','El usuario ' + currentUser.usuario + ' se encuentra desactivado')

        if not currentUser.isRecuperarContrasenia:
            raise Exception('N', 'No tenemos una solicitud para recuperar contraseña')
        
        passnew = data.get('pass')
        passConfirm = data.get('passConfirm')

        if passnew != passConfirm:
            raise Exception('N','La nueva contraseña y su confirmación no coinciden')    

        currentUser.isRecuperarContrasenia = False
        currentUser.contraseniaUsuario = passnew
        saveEntidadSinCommit(currentUser)
        Commit()
        return ResponseOkmsg('Contraseña recuperada exitosamente')
    except Exception as e:
        return ResponseException(e)


def accountUser(data):
    try:
        filtro = data.get('atributo')
        valor = data.get('valor').lower()

        email = 'email'
        usuario = 'usuario'
        contraseniaUsuario = 'contraseniaUsuario'

        if not (filtro == email or filtro ==usuario or filtro ==contraseniaUsuario):
            raise Exception('N','El atributo puede ser email, usuario o contraseniaUsuario')
        
        if filtro == email:
            hlCheckEmail(valor)
        
        if filtro == usuario:
            hlCheckUsuario(valor)
        
        if filtro == contraseniaUsuario:
            hlCheckPass(valor)

        return ResponseOk()
    except Exception as e:
        return ResponseException(e)    


def hlformatToken(token):
    token = token.replace("b'",'')
    token = token.replace("'",'')
    return str(token)


def hlCheckEmail(email):
    usuario = getUsuarioByEmail(email)
    if not usuario == None:
        raise Exception('N','El email: ' + email +', no se encuentra disponible')
    return 

def hlCheckUsuario(user):
    usuario = getUsuarioByUsuario(user)
    if not usuario == None:
        raise Exception('N','El usuario: ' + user +', no se encuentra disponible')
    return

def hlCheckPass(contraseniaUsuario):
    if len(contraseniaUsuario)<6:
       raise Exception('N','La contraseña debe ser mayor a 6 caracteres')
    return
