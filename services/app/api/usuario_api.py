from app.api.helperApi.hlUrl import urlUsuario
from flask import jsonify, request, make_response
from flask_restplus import Resource
from app.uses_cases.moduloSeguridad.gestionarUsuarios import postUser,getAllUsers, getUsuario, updateUsuario
from app.api.shared.tokenHandler import token_required

users = urlUsuario

@users.route('')
class UsersHandler(Resource):
    @token_required
    def post(self,currentUser):
        if (currentUser.rol.nombre =='administrador'):            
            print(self.keys())
            return postUser(self)
        else:
            return make_response(jsonify({'message:':'No posee permisos para realizar esta acción'}),404)

    @token_required
    def get(self,currentUser):
        if (self.rol.nombre=='administrador'):            
            return getAllUsers()
        else:
            return make_response(jsonify({'message:':'No posee permisos para realizar esta acción'}),404)

@users.route('/<string:cod>')
class UsersHandler(Resource):
    @token_required
    def get(self, currentUser,cod):
        if (currentUser.rol.nombre=='administrador'):            
            return getUsuario(cod)  
        else:
            return make_response(jsonify({'message:':'No posee permisos para realizar esta acción'}),404)

    @token_required
    def put(self,currentUser,cod):
        if (self.rol.nombre=='administrador'):            
            data = self.api.payload
            return updateUsuario(data, cod)
        else:
            return make_response(jsonify({'message:':'No posee permisos para realizar esta acción'}),404)

""" @users.route('/current')
class UsersHandler(Resource):
    def get(self, currentUser): """

  