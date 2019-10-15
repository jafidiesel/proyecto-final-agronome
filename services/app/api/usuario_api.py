from app.api.helperApi.hlUrl import urlUsuario
from flask import request,make_response,jsonify
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
        if (currentUser.rol.nombre =='administrador'):            
            return postUser(data)
        else:
            return make_response(jsonify({'message:':'No posee permisos para realizar esta acción'}),404)

    @token_required
    def get(data,currentUser):
        #isCheck = checkUrl(request.method,request.path,currentUser.rol.nombre)
        if (currentUser.rol.nombre =='administrador'):                         
            return getAllUsers()
        else:
            return make_response(jsonify({'message:':'No posee permisos para realizar esta acción'}),404)

@users.route('/<string:cod>')
class UsersHandler(Resource):
    @token_required
    def get(data,currentUser,cod):
        if (currentUser.rol.nombre=='administrador'):            
            return getUsuario(cod)  
        else:
            return make_response(jsonify({'message:':'No posee permisos para realizar esta acción'}),404)

    @token_required
    def put(data,currentUser,cod):
        if  (currentUser.rol.nombre=='administrador'):            
            return updateUsuario(data, cod)
        else:
            return make_response(jsonify({'message:':'No posee permisos para realizar esta acción'}),404)

""" @users.route('/current')
class UsersHandler(Resource):
    def get(self, currentUser): """

  