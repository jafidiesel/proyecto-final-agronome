from app.api.nomenclador_api import nomenclador
from app.api.parametro_api import parametro
from app.api.entidadInterm_api import entidadInterm
from app.api.actividad_api import actividad
from app.api.usuario_api import users
from app.api.login_api import loginUser
from app.api.finca_api import finca
from app.api.recomendacion_api import recomendacion
from app.api.analisis_api import analisis
from app.api.plan_api import plan
from app.api.planificacion_api import planificacion,parcelas
from app.api.reporte_api import  reporte
from app.api.grupo_planificacion_api import grupoPlanificacion
from app.api.libroCampo_api  import libroCampo

NAMESPACES = [
    nomenclador,
    parametro,
    entidadInterm,
    actividad,
    users,
    loginUser,
    finca,
    recomendacion,
    analisis,
    plan,
    planificacion,
    reporte,
    grupoPlanificacion,
    libroCampo,
    parcelas
]