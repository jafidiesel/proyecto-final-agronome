from app.api.helperApi.hlUrl import urlUsuario
from flask import jsonify
from flask_restplus import Resource
from app.uses_cases.moduloSeguridad.gestionarUsuarios import postUser

users = urlUsuario

@users.route('/')
class UsersHandler(Resource):
    def post(self):
        print("En post")
        data = self.api.payload
        return postUser(data)

''' data = {user: "nombre" ,email: "email", psw: "psw", isActiv: "", codRol: valor }'''