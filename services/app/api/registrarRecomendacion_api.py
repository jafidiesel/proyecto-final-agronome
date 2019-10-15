from flask_restplus import Resource
from app.api.helperApi.hlUrl import urlRegistrarRecom
from app.uses_cases.moduloRecomendacion.registrarRecomendacion import postRegistrarRecom


registrarRecom = urlRegistrarRecom

@registrarRecom.route('')
class RegistrarRecomHandler(Resource):
    def post(self):
        data = self.api.payload
        return postRegistrarRecom(data)