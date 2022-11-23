from datetime import datetime
import re
from tkinter import *
from controllerEstadia import clienteExistente
from mensaje import mensaje

# Se reciben por parametros los datos de la estadia
# Funcion del boton registrar la estadia
def registrarEstadia(fechaActual, habitacion, pension, fechaLimite, acompañantes, precio, nroDocumento, nombreCliente, tipoDocumento, pais, mail, poseeVehiculo, patente, marca, ventana: Tk, archivo = open("RegistroEstadia.txt", "a", encoding = "utf-8")):
    # Datos Estadia
    # _fechaActual = ventana.entryFechaActual.get()
    # _habitacion = ventana.entryHabitacion.get()
    # _pension = ventana.entryPension.get()
    # _fechaLimite = ventana.entryFechaLimite.get()
    # _acompañantes = ventana.entryAcompañantes.get()
    # _precio = ventana.entryPrecio.get()
    # _numeroDocumentoCliente = ventana.entryNumeroDocumento.get()
    _regexMail = r"[\S(a-z0-9!)]+[\S(a-z!)]*.+(.com|([^0-9][a-z]*))$"
    # La estadia guarda solo el dni para consultar por ese dato unico
    # Verifica que los datos solicitados estén completados
    if not (habitacion == "" or pension == "" or fechaLimite == "" or acompañantes == ""):
        if nombreCliente == "" or nroDocumento == "" or tipoDocumento == "" or pais == "" or poseeVehiculo == "":
            mensaje("El cliente necesita ser seleccionado.\n\rPor favor, ingrese los datos necesarios.", "ERROR")
        else:
            if ((mail != "") and 
                # Valida el mail con la expresion regular
                # Verifica que solo exista un caracter '@'
            not ((re.search(_regexMail, mail)) and (len(mail.split("@")) == 2) and (len(mail.split("@")[0]) > 0))):
                # En caso de no ser correcto
                mensaje(mensaje = "El mail ingresado no es correcto. Verifique la entrada.", titulo = "ERROR")
            else:
            # En caso de tener los campos correctos, los registra
                registrarCliente(nroDocumento, nombreCliente, tipoDocumento, pais, mail, poseeVehiculo, patente, marca)
                registrarDatosEnArchivo(fechaActual + "," + habitacion + "," + pension + "," + fechaLimite + "," + acompañantes + "," + precio + "," + nroDocumento +"," + patente + "," + marca + "," + "PendienteCobro,"+ str(obtenerCantidadDiasReserva(fechaActual, fechaLimite)) + "\n", archivo)
                mensaje("La estadia se ha registrado con éxito.", "Estadia registrada")
    else:
        mensaje("La estadia no contiene datos.\n\rSeleccione los datos requeridos.", "ERROR")
    ventana.destroy()

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
        mensaje("Los datos del vehiculo no pueden ser nulos.\n\rSeleccione los datos del vehiculo.", "ERROR")
    if not clienteExistente(nroDocumento):
        registrarDatosEnArchivo(nroDocumento + "," + nombreCompleto + "," + tipoDocumento + "," + pais + "," + mail + "," + poseeVehiculo + "," + patente + "\n", archivo)
        mensaje("El cliente ha sido registrado con éxito.", "Cliente registrado")

def registrarVehiculo(patente, marca, archivo = open("Vehiculo.txt", "a", encoding = "utf-8")):
    # Datos Vehiculo
    # _patente = ventana.entryPatente.get()
    # _marca = ventana.entryMarca.get()
    registrarDatosEnArchivo(patente + "," + marca + "\n", archivo)
    mensaje("El vehiculo ha sido registrado con éxito.", "Vehiculo registrado")

def registrarDatosEnArchivo(datos: str, archivo: str):
    """
    Registra los datos en el archivo ingresado por parámetro y le añade en una nueva linea al final
    Los datos que se reciben por parámetro
    """
    archivo.write(datos)
    archivo.close()

def obtenerCantidadDiasReserva(fechaDesde: str, fechaHasta: str):
    return (datetime.strptime(fechaHasta, "%d/%m/%Y") - datetime.strptime(fechaDesde, "%d/%m/%Y")).days