from flask import jsonify
from flask_restplus import Resource
from app.api.helperApi.hlUrl import urlActivParam
from app.uses_cases.moduloConfiguracion.gestionarActivParam import postActivParam
#from app.uses_cases.moduloConfiguracion.gestionarNomenclador import getNomenclador, getNomencladoCod, postNomenclador, putNomenclador


activParam = urlActivParam

@activParam.route('')
class ActivParamHandler(Resource):
    def post(self):
        data = self.api.payload
        print(data)
        return postActivParam(data)
    