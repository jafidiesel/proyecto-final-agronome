from app.api.helperApi.hlUrl import urlUsuario
from flask import jsonify
from flask_restplus import Resource
from app.uses_cases.moduloSeguridad.gestionarUsuarios import postUser,getAllUsers, getUsuario

users = urlUsuario

@users.route('')
class UsersHandler(Resource):
    def post(self):
        print("En post")
        data = self.api.payload
        return postUser(data)
    def get(self):
        return getAllUsers()

@users.route('/<string:cod>')
class UsersHandler(Resource):
    def get(self, cod):
        return getUsuario(cod)