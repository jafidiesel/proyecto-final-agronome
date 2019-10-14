#/login
from app.api.helperApi.hlUrl import urlLogin
from flask_restplus import Resource
from app.uses_cases.moduloSeguridad.login import login,logout
from app.api.shared.tokenHandler import token_required

loginUser = urlLogin
@loginUser.route('')

class LoginHandler(Resource):
    def post(self):
        print('En post')
        data = self.api.payload
        return login(data)
    @token_required
    def get(self,dataUser):
        userCode = self.cod
        print(userCode)
        return logout(userCode)
