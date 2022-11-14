from tkinter import *

from mensajeExito import mensaje


# Se reciben por parametros los datos de la estadia
# Funcion del boton registrar la estadia
def registrarEstadia(fechaActual, habitacion, pension, fechaLimite, acompañantes, precio, nroDocumento, nombreCliente, tipoDocumento, pais, mail, poseeVehiculo, patente, marca, archivo = open("RegistroEstadia.txt", "a", encoding = "utf-8")):
    # Datos Estadia
    # _fechaActual = ventana.entryFechaActual.get()
    # _habitacion = ventana.entryHabitacion.get()
    # _pension = ventana.entryPension.get()
    # _fechaLimite = ventana.entryFechaLimite.get()
    # _acompañantes = ventana.entryAcompañantes.get()
    # _precio = ventana.entryPrecio.get()
    # _numeroDocumentoCliente = ventana.entryNumeroDocumento.get()
    # La estadia guarda solo el dni para consultar por ese dato unico
    # Verifica que los datos solicitados estén completados
    if not (habitacion == "" or pension == "" or fechaLimite == "" or acompañantes == ""):
        if nombreCliente == "" or nroDocumento == "" or tipoDocumento == "" or mail == "" or pais == "" or poseeVehiculo == "":
            mensaje("El cliente necesita ser seleccionado.\n\rPor favor, ingrese los datos necesarios.")
        else:
            # En caso de tener los campos correctos, los registra
            registrarCliente(nroDocumento, nombreCliente, tipoDocumento, pais, mail, poseeVehiculo, patente, marca)
            registrarDatosEnArchivo(fechaActual + "," + habitacion + "," + pension + "," + fechaLimite + "," + acompañantes + "," + precio + "," + nroDocumento + "," + "PendienteCobro \n", archivo)
            mensaje("La estadia se ha registrado con éxito.")
    else:
        mensaje("La estadia no contiene datos.\n\rSeleccione los datos requeridos.")

def registrarCliente(nroDocumento, nombreCompleto, tipoDocumento, pais, mail, poseeVehiculo, patente, marca, archivo = open("Cliente.txt", "r", encoding = "utf-8")):        
    # Datos Cliente
    # _numeroDocumentoCliente = ventana.entryNumeroDocumento.get()
    # _nombreYApellido = ventana.entryNombreYApellido.get()
    # _tipoDocumento = ventana.entryTipoDocumento.get()
    # _pais = ventana.entryPais.get()
    # _mail = ventana.entryMail.get()
    # _poseeVechiculo = ventana.entryPoseeVehiculo.get()
    # El cliente conoce la patente de su vehiculo
    # _patente = ventana.entryPatente.get()
    if not clienteExistente(nroDocumento):
        if (poseeVehiculo == "SI" and patente != "" and marca != ""):
            registrarVehiculo(patente, marca)
        elif poseeVehiculo == "NO":
            pass
        else:
            mensaje("Los datos del vehiculo no pueden ser nulos.\n\rSeleccione los datos del vehiculo.")
        registrarDatosEnArchivo(nroDocumento + "," + nombreCompleto + "," + tipoDocumento + "," + pais + "," + mail + "," + poseeVehiculo + "," + patente + "\n", archivo)
        mensaje("El cliente ha sido registrado con éxito.")

def registrarVehiculo(patente, marca, archivo = open("Vehiculo.txt", "a", encoding = "utf-8")):
    # Datos Vehiculo
    # _patente = ventana.entryPatente.get()
    # _marca = ventana.entryMarca.get()
    registrarDatosEnArchivo(patente + "," + marca + "\n", archivo)
    mensaje("El vehiculo ha sido registrado con éxito.")

def registrarDatosEnArchivo(datos: str, archivo: str):
    """
    Registra los datos en el archivo ingresado por parámetro y le añade en una nueva linea al final
    Los datos que se reciben por parámetro
    """
    archivo.write(datos)
    archivo.close()

# # Funcion recursiva para obtener la lista de cada uno de los archivos de texto
# def para(lista: list, lineasCorregidas : list = [], i : int = 0):
#     # Quita el salto de linea de cada linea
#     lineasCorregidas.append(str(lista[i][0:len(lista[i])-1]))
#     # Al llegar al limite de lineas (cuando el indice es igual a la longitud de la lista), finaliza la funcion
#     if i == len(lista) - 1:
#         return lineasCorregidas
#     else:
#         i += 1
#         para(lista, lineasCorregidas, i)

def calcularPrecioEstadia(pension: str, precio: int = 0):
    """
    Funcion que calcula el precio de la estadia segun el tipo de pensión seleccionada\n
    Parametros (\npension -> pension seleccionada en la pantalla\nprecio -> variable local opcional para definir el precio\n)
    Retorna el valor del precio
    """
    if pension == "Desayuno":
        precio = 850
    elif pension == "Media Pension":
        precio = 1000
    else:
        precio = 1500
    return precio


# Retorna
def consultar(lineas: list, opciones: list = [], i: int = 0):
    """
    Funcion generica que recibe las lineas de los archivos de texto
    Retorna las opciones que se cargan en los combos de la vista
    """ 
    if len(opciones) > 0 and i == 0:
        opciones.clear()
    opciones.append(str(lineas[i][0:-1]))
    i += 1
    if not (i == len(lineas)):
        consultar(lineas, opciones, i)
    return tuple(opciones)

def buscarDocumento(nroDocumento, archivo, lineas: list, indice:int = 0):
    """
    Funcion que busca el documento del cliente para validar su existencia\n\r
    Retorna true en caso de exitir el documento del cliente.\n
    Parametros(nroDocumento -> numero de documento del cliente, archivo -> archivo que se lee, lineas -> lineas del archivo, indice -> numero para recorrer las lineas)
    """
    # Cada indice de lineas es una linea del archivo y se lo splitea guardandolo como vector por comas "," además se lo compara con el numero de documento ingresado por pantalla y si es igual se devuelve True, es decir que ya está registrado.
    if indice == len(lineas):
        archivo.close()
        return False
    if lineas[indice].count(nroDocumento) == 1:
        archivo.close()
        return True
    indice += 1
    buscarDocumento(nroDocumento, lineas, indice)

def clienteExistente(nroDocumento: str, archivo = open("Cliente.txt", "r", encoding = "utf-8")):
    """
    Llama a la funcion buscarDocumento\n\r
    Parametros(nroDocumento -> numero de documento del cliente | archivo -> archivo que lee)
    """
    # xd = list(filter(lambda linea : linea.split(",")[0] == nroDocumento, archivo.readlines()))
    return True if len(list(filter(lambda linea : linea.split(",")[0] == nroDocumento, archivo.readlines()))) != 0 else False and archivo.close()