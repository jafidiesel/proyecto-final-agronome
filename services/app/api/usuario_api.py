from app.api.helperApi.hlUrl import urlUsuario
from flask import jsonify, request, make_response
from flask_restplus import Resource
from app.uses_cases.moduloSeguridad.gestionarUsuarios import postUser,getAllUsers, getUsuario, updateUsuario

users = urlUsuario

@users.route('')
class UsersHandler(Resource):
    def post(self):
        data = self.api.payload
        return postUser(data)
    def get(self):
        return getAllUsers()
    def put(self):
        data = self.api.payload
        return updateUsuario(data)

@users.route('/<string:cod>')
class UsersHandler(Resource):
    def get(self, cod):
        return getUsuario(cod)

""" @users.route('/login')
class UsersHandler(Resource):
    #auth = request.authorization
 """    