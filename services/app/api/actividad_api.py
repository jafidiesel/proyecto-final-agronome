from flask import jsonify
from flask_restplus import Resource
from app.api.helperApi.hlUrl import urlOpcion
from app.api.helperApi.hlDb import saveEntidad, selectAll, selectCod
from app.model.hlmodel import Actividad


opcion = urlActividad

@opcion.route('')
class OpcionsHandler(Resource):
    def get(self):
        return selectAll(Actividad)

    def post(self):
        data = self.api.payload
        actividad = Actividad.from_json(data)
        return saveEntidad(actividad)


@opcion.route('/<int:id>')
class OpcionHandler(Resource):
    def get(self, id):
        return selectByCod(Actividad,id) #solo funciona para codOpcion 