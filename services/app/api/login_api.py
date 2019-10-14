#/login
from app.api.helperApi.hlUrl import urlLogin
from flask_restplus import Resource
from app.uses_cases.moduloSeguridad.login import login,logout
from app.api.shared.tokenHandler import token_required

loginUser = urlLogin
@loginUser.route('')

class LoginHandler(Resource):
    def post(self):
        data = self.api.payload
        print(data)
        return login(data)
    @token_required
    def delete(self,dataUser):
        userCode = self.cod
        print(userCode)
        return logout(userCode)
