#/login
from app.api.helperApi.hlUrl import urlLogin
from flask_restplus import Resource
from app.uses_cases.moduloSeguridad.login import login


loginUser = urlLogin
print(loginUser)
@loginUser.route('')
class LoginHandler(Resource):
    def post(self):
        print('En post')
        data = self.api.payload
        return login(data)
    def get(self):
        print('En GET')
        return True
#/singup
#/logout