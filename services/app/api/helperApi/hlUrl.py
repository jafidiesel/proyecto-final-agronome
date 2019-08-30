#definiciones de las rutas
from flask_restplus import Namespace

#modulo de configuraciones"
URL_MC = 'api/configuracion/'
urlOpcion = Namespace(URL_MC + 'opcion')
urlEstadoPlanificacion= Namespace(URL_MC + 'estadoPlanificacion')
urlNomenclador = Namespace(URL_MC + 'nomenclador')

#modulo de recursos
URL_MC = 'api/recurso/'

