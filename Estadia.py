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

def registrarCliente(nroDocumento, nombreCompleto, tipoDocumento, pais, mail, poseeVehiculo, patente, marca, archivo = open("Cliente.txt", "a", encoding = "utf-8")):        
    # Datos Cliente
    # _numeroDocumentoCliente = ventana.entryNumeroDocumento.get()
    # _nombreYApellido = ventana.entryNombreYApellido.get()
    # _tipoDocumento = ventana.entryTipoDocumento.get()
    # _pais = ventana.entryPais.get()
    # _mail = ventana.entryMail.get()
    # _poseeVechiculo = ventana.entryPoseeVehiculo.get()
    # El cliente conoce la patente de su vehiculo
    # _patente = ventana.entryPatente.get()
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
    archivo.write(datos)
    archivo.close()

def consultarTipoDocumento(archivo = open("TipoDocumento.txt", "r", encoding = "utf-8")):
    return para(archivo.readlines())

def consultarMarcas(archivo = open("MarcasVehiculo.txt", "r", encoding = "utf-8")):
    return para(archivo.readlines())

def consultarHabitaciones(archivo = open("Habitaciones.txt", "r", encoding = "utf-8")):
    return para(archivo.readlines())

def consultarPensiones(archivo = open("Pension.txt", "r", encoding = "utf-8")):
    return para(archivo.readlines())

# Funcion recursiva para obtener la lista de cada uno de los archivos de texto
def para(lista: list, lineasCorregidas : list = [], indice : int = 0):
    # Quita el salto de linea de cada linea
    lineasCorregidas.append(str(lista[indice][0:len(lista[indice])-1]))
    # Al llegar al limite de lineas (cuando el indice es igual a la longitud de la lista), finaliza la funcion
    if indice == len(lista) - 1:
        return tuple(lineasCorregidas)
    indice += 1
    para(lista, lineasCorregidas, indice)

def calcularPrecioEstadia(pension: str, precio: Entry):
    if pension == "Desayuno":
        return precio.insert(0, "850")
    elif pension == "Media Pension":
        return precio.insert(0, "1000")
    else:
        return precio.insert(0, "1500")