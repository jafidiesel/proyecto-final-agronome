from flask_restplus import Resource
from app.api.helperApi.hlUrl import urlFinca
from app.uses_cases.moduloGestionFinca.gestionarFinca import postFinca, getFincaCod , getFinca


finca = urlFinca

@finca.route('')
class FincaHandler(Resource):
    def post(self):
        data = self.api.payload
        return postFinca(data)

    def get(self):
        return getFinca()

@finca.route('/<int:codFinca>')
class FincaHandler(Resource):
    def get(self,codFinca):
        return getFincaCod(codFinca)
