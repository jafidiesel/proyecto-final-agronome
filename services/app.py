import os
from flask_migrate import MigrateCommand
from flask_script import Manager, Server
from app.backend import create_api
from app.model import hlmodel
#from app.model.opcion import Opcion # creo qeu no hace falta esto
#from app.model.estadoPlanificacion import EstadoPlanificacion
#from app.model.tipoPlanificacion import TipoPlanificacion
#from app.model.tipoAnalisis import TipoAnalisis
#from app.model.tipoDato import TipoDato
#from app.model.tipoParametro import TipoParametro
#from app.model.actividad import Actividad
#from app.model.permiso import Permiso
#from app.model.tipoPlan import TipoPlan
#from app.model.parametro import Parametro



#el metodo create api es un metodo que crea traido del archivo backend

app = create_api(os.getenv('FLASK_CONFIG') or 'default')


if __name__ == '__main__':
    manager = Manager(app)
    manager.add_command('db',MigrateCommand)
    manager.add_command("runserver", Server(threaded=bool(int(os.environ.get('THREADED'))), port=int(os.environ.get('PORT'))))

    manager.run(default_command='runserver')