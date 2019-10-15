import re
from app.api.helperApi.hlUrl import urlNomenclador,urlEntidadInterm, urlParametro, urlEntidadInterm,urlResgistrarActiv,  urlUsuario, urlLogin
def checkUrl(method,pat,rol):
    urlAux = method + pat #armo url
    nro = re.sub("\D", "", urlAux) #busco si tiene algun numero
    url = re.sub(nro,"",urlAux)
    print(urlAux)
    print (url)
    print(nro)
    isCheck = False
    
    #Modulo Configuracion
    #nomenclador
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

    #entidad Intermedia Asociaciones  OJO PORQUE HAY QUE VER QUE RECIBE LA INTERMEDIA
    MCASO = '/'  + urlEntidadInterm.name


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

    #Login
    MSLOG = '/' + urlLogin.name
    MSLOG_DELETE = 'DELETE' + MSLOG


    print(MCNOM_GET)


    administrador = (MSUSU_POST,MSUSU_GETS,MSUSU_GET,MSUSU_PUT,MSLOG_DELETE,
        MCPAR_POST,MCPAR_GETS,
        MAREG_GET,MAREG_PUT,
        MCNOM_POST,MCNOM_GETS,MCNOM_GET,MCNOM_PUT)

    encargadofinca = ()#(MSUSU_POST,MSUSU_GETS,MSUSU_GET,MSUSU_PUT)



    if rol == 'administrador':
        isCheck = url in administrador
    else:
        if rol == 'encargadofinca':
            isCheck = url in encargadofinca


    return isCheck
    