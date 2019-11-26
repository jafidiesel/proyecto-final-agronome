def cultivoFullToDict(cultivo):
    dtoCultivo = dict(
        cod                = cultivo.cod,     
        cantidadCultivo    = cultivo.cantidadCultivo,    
        produccionEsperada = cultivo.produccionEsperada, 
        variedadCultivo    = cultivo.variedadCultivo,    
        cicloUnico         = cultivo.cicloUnico,
        codTipoCultivo     = cultivo.tipoCultivoR.cod,  
        nombreTipoCultivo  = cultivo.tipoCultivoR.nombre       
    )
    return dtoCultivo


def libroCampoToDict(libroCampo): ##se usa en el detalle de la actividad
    dtoLibroCampo = dict(
        codLibroCampo     = libroCampo.codLibroCampo,
        nombreLibroCampo  = libroCampo.nombreLibroCampo
    )
    return dtoLibroCampo


def libroCampoFullToDict(libroCampo): 
    dtoLibroCampo = dict(
        codLibroCampo     = libroCampo.codLibroCampo,
        nombreLibroCampo  = libroCampo.nombreLibroCampo,
        fchIni            = hlFch(libroCampo.fchIni),
        fchFin            = hlFch(libroCampo.fchFin),
        cultivo           = cultivoFullToDict(libroCampo.cultivo)
    )
    return dtoLibroCampo


def libroCampoListFullToDict(libroCampoList):
    dtoLibroCampoList = []

    for libroCampo in libroCampoList:
        dtoLibroCampo =  libroCampoFullToDict(libroCampo)
        dtoLibroCampoList.append(dtoLibroCampo)

    return dtoLibroCampoList


def hlFch(fch): #helper por si la fecha es null
    fchOut = ''
    if not fch == None:
        fchOut = fch.strftime("%d-%m-%Y %H:%M:%S") 
    return fchOut