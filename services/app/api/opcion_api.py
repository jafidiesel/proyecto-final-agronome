from flask import jsonify
from flask_restplus import Resource
from app.api.helperApi.hlUrl import urlOpcion
from app.api.helperApi.hlDb import saveEntidad, selectAll, selectCod
from app.model.opcion import Opcion


opcion = urlOpcion

@opcion.route('')
class OpcionsHandler(Resource):
    def get(self):
        return selectAll(Opcion)

    def post(self):
        data = self.api.payload
        opcion = Opcion.from_json(data)
        return saveEntidad(opcion)


@opcion.route('/<int:id>')
class OpcionHandler(Resource):
    def get(self, id):
        return selectCod(Opcion,id) #solo funciona para codOpcion 
    