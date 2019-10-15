import re
from app.api.helperApi.hlUrl import urlNomenclador,urlEntidadInterm, urlParametro, urlEntidadInterm,urlResgistrarActiv,  urlUsuario
def checkUrl(method,pat,rol):
    urlAux = method + pat #armo url
    nro = re.sub("\D", "", urlAux) #busco si tiene algun numero
    url = re.sub(nro,"",urlAux)
    isCheck = False
    
    #Modulo Configuracion
    #nomenclador

    if url.index('/api/configuracion/nomenclador/')>0: 
        ##macheamos la url con el post y el get ya que la url se reutiliza para todas las entidades
        url = 'GET/api/configuracion/nomenclador/'
    MCNOM = '/' + urlNomenclador.name
    MCNOM_POST = 'POST' + MCNOM
    MCNOM_GETS = 'GET' + MCNOM
    MCNOM_GET = MCNOM_GETS  + '/'
    MCNOM_PUT = 'PUT' + MCNOM + '/'

    #parametro
    MCPAR = '/' + urlParametro.name
    MCPAR_POST = 'POST' + MCPAR
    MCPAR_GETS = 'GET' + MCPAR
    MCPAR_GET = MCPAR_GETS  + '/'
    MCPAR_PUT = 'PUT' + MCPAR + '/'

    #entidad Intermedia Asociaciones 
    #if url.index('/api/configuracion/asociar/')>0: 
        ##macheamos la url con el post y el get ya que la url se reutiliza para todas las entidades
    #    url = 'GET/api/configuracion/asociar/'
    
    MCASO = '/'  + urlEntidadInterm.name
    MCASO_POST = 'POST' + MCASO
    MCASO_GETS = 'GET' + MCASO
    MCASO_GET = MCASO_GETS  + '/'
    MCASO_PUT = 'PUT' + MCASO + '/'
    

    #Modulo Actividades
    #Registrar Actividades
    MAREG = '/' + urlResgistrarActiv.name
    MAREG_POST = 'POST' + MAREG
    MAREG_GETS = 'GET' + MAREG
    MAREG_GET = MAREG_GETS  + '/'
    MAREG_PUT = 'PUT' + MAREG + '/'


    ##Modulo Seguridad
    #usuario
    MSUSU = '/' + urlUsuario.name
    MSUSU_POST = 'POST' + MSUSU
    MSUSU_GETS = 'GET' + MSUSU
    MSUSU_GET = MSUSU_GETS + '/'
    MSUSU_PUT = 'PUT' + MSUSU + '/' 





    administrador = (MSUSU_POST,MSUSU_GETS,MSUSU_GET,MSUSU_PUT)
    
    encargadofinca = (
        MSUSU_POST,MSUSU_GETS,MSUSU_GET,MSUSU_PUT, #MS
        MCNOM_POST,
        MCNOM_GET
        )



    if rol == 'administrador':
        isCheck = url in administrador
    else:
        if rol == 'encargadofinca':
            isCheck = url in encargadofinca

    print('url auxiliar: ' + urlAux)
    print ('url sin numeros: ' + url)

    return isCheck
    