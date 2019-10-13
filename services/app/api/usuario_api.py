from app.api.helperApi.hlUrl import urlUsuario
from flask import jsonify, request, make_response
from flask_restplus import Resource
from app.uses_cases.moduloSeguridad.gestionarUsuarios import postUser,getAllUsers, getUsuario, updateUsuario
from app.api.shared.tokenHandler import token_required

users = urlUsuario

@users.route('')
class UsersHandler(Resource):
    def post(self):
        data = self.api.payload
        return postUser(data)

    #@token_required
    def get(self):
        return getAllUsers()
    
@users.route('/<string:cod>')
class UsersHandler(Resource):
    def get(self, cod):
        return getUsuario(cod)
    def put(self, cod):
        data = self.api.payload
        return updateUsuario(data, cod)

  