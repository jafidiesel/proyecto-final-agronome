#/login
from app.api.helperApi.hlUrl import urlLogin
from flask_restplus import Resource
from app.uses_cases.moduloSeguridad.login import login,logout, solicitarReinicioPsw, resetPsw
from app.api.shared.tokenHandler import token_required
from flask import jsonify,make_response
from app.api.helperApi.hlResponse import notCheck
from app.uses_cases.moduloSeguridad.checkUrl import checkUrl
from flask import request

loginUser = urlLogin
@loginUser.route('')
class LoginHandler(Resource):
    def post(self):
        data = self.api.payload
        print(data)
        return login(data)
    @token_required
    def delete(data,currentUser):
        isCheck = checkUrl(request.method,request.path,currentUser.rol.nombre)
        if isCheck:            
            userCode = currentUser.cod
            return logout(userCode)
        else:
            return make_response(jsonify({'message:':'No posee permisos para realizar esta acción'}),404)

@loginUser.route('/reset')
class LoginHandler(Resource):
    def post(self):
        data = self.api.payload
        return solicitarReinicioPsw(data)
    def get(self):
        data = self.api.payload
        return resetPsw(data)