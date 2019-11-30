from app.api.helperApi.hlResponse import ResponseException
from app.model.hlmodel import Finca, Parcela, Cuadro, FincaUsuario
from app.repositorio.hlDb import saveEntidadSinCommit, Commit , deleteObject
from app.repositorio.repositorioGestionarFinca import selectFincaCod, selectFinca
from app.uses_cases.moduloConfiguracion.gestionarNomenclador import getNomencladoCod
from app.api.helperApi.hlResponse import ResponseException, ResponseOk, ResponseOkmsg

def postFinca(data,currentUser):
    try:
        nombreFinca =data.get('nombre')
        superficie = data.get('superficie')
        parcelaList = data.get('parcelas')
        calle = data.get('calle')
        nro = data.get('nro')
        localidad = data.get('localidad')
        provincia = data.get('provincia')

        isActiv = True
       
        finca = Finca(nombreFinca = nombreFinca, superficie = superficie ,isActiv = isActiv, calle=calle, nro=nro, localidad=localidad, provincia = provincia)
        
        for parcelaItem in parcelaList:
            nombreParcela = parcelaItem.get('nombre')
            superficieParcela = parcelaItem.get('superficie')
            filas = parcelaItem.get('filas')
            columnas = parcelaItem.get('columnas')

            parcela = Parcela(nombrePacela = nombreParcela, superficieParcela=superficieParcela, filas =filas,columnas=columnas)

            #Cuadros
            for i in range(1,(filas+1)):
                for j in range(1,(columnas+1)):
                    nombreCuadro = nombreParcela + str(i) + str(j)
                    cuadro = Cuadro(nombreCuadro=nombreCuadro)    

                    parcela.cuadroList.append(cuadro) #asociacion de parcela -> cuadro

            finca.parcelaList.append(parcela) #asociacion de finca -> parcela
        

        ##asignación de usuario con finca, esto se hace solo con el encargado, ya que el admin tambien puede crear finca, pero asignarce no puede
        rol = currentUser.rol.nombre

        if rol == 'encargadofinca':
            fincaUsuario = FincaUsuario(isActiv=True) # creo la finca usuario
            fincaUsuario.finca = finca #asociación de finca
            currentUser.fincaUsuarioList.append(fincaUsuario) # asociación


        saveEntidadSinCommit(finca)
        Commit()

        dtoResult = dict(codFinca=finca.codFinca, nombreFinca = finca.nombreFinca)

        return ResponseOkmsg(dtoResult)
    except Exception as e:
        return ResponseException(e)

def getFinca():
    fincaList = selectFinca()
    dtoFincaList = []

    for finca in fincaList:
        dtoFincaAux = fincaToDicc(finca)
        dtoFincaList.append(dtoFincaAux)

    return dict(finca=dtoFincaList)

def getFincaCod(codFinca):
    try:    
        finca = selectFincaCod(codFinca)
        if not finca: 
            raise Exception('N','No existe finca con código ' + str(codFinca))

        dtoFinca = fincaToDicc(finca)
        parcelaList = finca.parcelaList
        dtoParcelaList = []

        for parcela in parcelaList:
            dtoParcelaAux = dict(codParcela = parcela.codParcela, nombre = parcela.nombrePacela, superficie = str(parcela.superficieParcela) + ' m', filas= parcela.filas, columnas = parcela.columnas, cantCuadros = parcela.filas * parcela.columnas)

            cuadroList = parcela.cuadroList
            dtoCuadroList = []
            for cuadro in cuadroList:
                dtoCuadroAux = dict(codCuadro = cuadro.codCuadro, nombreCuadro = cuadro.nombreCuadro)    
                dtoCuadroList.append(dtoCuadroAux)

            dtoParcelaAux['cuadros'] = dtoCuadroList
            dtoParcelaList.append(dtoParcelaAux)

        dtoFinca['parcelas'] = dtoParcelaList

        return (dict(finca=dtoFinca))       
    except Exception as e:
        return ResponseException(e)

def putFinca(data,codFinca):
    try:
        nombreFinca =data.get('nombre')
        superficie = data.get('superficie')
        parcelaListIn = data.get('parcelas')
        calle = data.get('calle')
        nro = data.get('nro')
        localidad = data.get('localidad')
        provincia = data.get('provincia')
        
        finca = selectFincaCod(codFinca)

        finca.nombreFinca = nombreFinca
        finca.superficie = superficie
        finca.calle = calle
        finca.nro = nro
        finca.localidad = localidad
        finca.provincia = provincia
        
        if True: #aca tengo que poner la logica para detectar si no esta en planificación
            parcelaList = finca.parcelaList
            for parcela in parcelaList:
                cuadroList = parcela.cuadroList
                for cuadro in cuadroList:
                    deleteObject(cuadro)
                deleteObject(parcela)
            
            Commit() #se hace este commit para eliminar fisicamente los registros

            #Creacion de parcelas y cuadros nuevos, esto se repite en el post
            for parcelaItem in parcelaListIn:
                nombreParcela = parcelaItem.get('nombre')
                superficieParcela = parcelaItem.get('superficie')
                filas = parcelaItem.get('filas')
                columnas = parcelaItem.get('columnas')

                parcela = Parcela(nombrePacela = nombreParcela, superficieParcela=superficieParcela, filas =filas,columnas=columnas)
                
                #Cuadros
                for i in range(1,(filas+1)):
                    for j in range(1,(columnas+1)):
                        nombreCuadro = nombreParcela + str(i) + str(j)
                        cuadro = Cuadro(nombreCuadro=nombreCuadro)    
                        
                        parcela.cuadroList.append(cuadro) #asociacion de parcela -> cuadro
                finca.parcelaList.append(parcela) #asociacion de finca -> parcela
        
            #saveEntidadSinCommit(finca)
            Commit()
            return ResponseOkmsg('Se han modificados los datos generales de la finca, con sus cuadros y parcelas ya que no se encuentran en uso')
        else:
            saveEntidadSinCommit(finca)
            Commit()
            return ResponseOkmsg('Se han modificados los datos generales de la finca, ya que los cuadros y parcelas se encuentran en uso')
    except Exception as e:
        return ResponseException(e)
    




def fincaToDicc(finca):
    calle = finca.calle
    nro = finca.nro
    localidad = finca.localidad
    provincia = finca.provincia
    urlMaps = adapterUrl(calle,nro,localidad,provincia)

    dtoFinca = dict(codFinca = finca.codFinca, nombre = finca.nombreFinca, superficie = finca.superficie, isActiv = finca.isActiv, calle= calle, nro = nro, localidad=localidad, provincia=provincia, urlMaps = urlMaps)
    return dtoFinca


def adapterUrl(calle,nro,localidad,provincia):
    urlMaps = 'https://www.google.com.ar/maps/place/' + calle + '+' + str(nro) + '+' + localidad + '+' + provincia
    urlMaps = urlMaps.replace(' ','+')
    return urlMaps


def getUsersByFinca(finca): #devuelve todos los usuarios(objetos) de una finca
    usuarioList = []
    fincaUsuarioList = finca.fincaUsuarioList

    for fincaUser in fincaUsuarioList:
        if fincaUser.fchFin == None and fincaUser.isActiv:
            usuarioList.append(fincaUser.usuario)
    return usuarioList


def getUsersByFincaFilter(finca,nombreRol): #devueve los usuarios(objetos) por filtro
    hlrol = {
        'administrador' : 1,
        'encargadofinca': 2,
        'ingeniero':3,
        'supervisor':4
        }

    usuario = ''
    usuarioList = getUsersByFinca(finca)
    rol = getNomencladoCod('rol',hlrol[nombreRol])

    for user in usuarioList:
        if user.rol == rol:
            usuario = user
            exit 

    return usuario
