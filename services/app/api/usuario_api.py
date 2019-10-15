from app.api.helperApi.hlUrl import urlUsuario
from flask import request
from flask_restplus import Resource
from app.uses_cases.moduloSeguridad.gestionarUsuarios import postUser,getAllUsers, getUsuario, updateUsuario
from app.uses_cases.moduloSeguridad.checkUrl import checkUrl
from app.api.shared.tokenHandler import token_required
from app.api.helperApi.hlResponse import notCheck
users = urlUsuario

@users.route('')
class UsersHandler(Resource):
    @token_required
    def post(data,currentUser):
        isCheck = checkUrl(request.method,request.path,currentUser.rol.nombre)
        if isCheck:
            return postUser(data)
        else:
            return notCheck()

    @token_required
    def get(data,currentUser):
        isCheck = checkUrl(request.method,request.path,currentUser.rol.nombre)
        if  isCheck:             
            return getAllUsers()
        else:
            return notCheck()

@users.route('/<string:cod>')
class UsersHandler(Resource):
    @token_required    
    def get(data,currentUser,cod):
        isCheck = checkUrl(request.method,request.path,currentUser.rol.nombre)
        if  isCheck: 
            return getUsuario(cod)  
        else:
            return notCheck()

    @token_required
    def put(data,currentUser,cod):
        isCheck = checkUrl(request.method,request.path,currentUser.rol.nombre)
        if  isCheck:            
            return updateUsuario(data, cod)
        else:
            return notCheck()

""" @users.route('/current')
class UsersHandler(Resource):
    def get(self, currentUser): """

  