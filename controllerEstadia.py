# En este archivo se realizan las conversiones de los datos y validaciones que corresponden a la pantalla

# region Imports
from mensaje import mensaje
import datetime
# endregion

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

def eliminarSaltoLinea(cadena: str):
    """
    Elimina el salto de linea para todas las cadenas que se reciben una vez se leen los archivos de texto
    """
    return cadena[0 : -1]

def validarFechas(fechaDesde: str, fechaHasta: str):
    """
    Se valida la fecha actual de la pantalla con la fecha fin ingresada
    """
    # En caso de no contar con el formato se indica el error
    if not (len(fechaHasta.split("/")) == 3):
        mensaje(titulo="ERROR", mensaje="El formato de la fecha no es el correcto.")
        return False
    else:
        # Verifica que la fecha actual sea menor a la final
        if not (datetime.datetime(
            int(fechaDesde.split("/")[2]),
            int(fechaDesde.split("/")[1]),
            int(fechaDesde.split("/")[0])) 
            <= 
            datetime.datetime(
            int(fechaHasta.split("/")[2]), 
            int(fechaHasta.split("/")[1]), 
            int(fechaHasta.split("/")[0]))):
            mensaje(mensaje="La fecha limite es menor a la fecha actual. Verifique la entrada de la misma.", titulo="ERROR")
            return False
        else:
            return True

def consultar(lineas: list, opciones: list = [], i: int = 0):
    """
    Funcion generica que recibe las lineas de los archivos de texto
    Retorna las opciones que se cargan en los combos de la vista
    """
    if len(opciones) > 0 and i == 0:
        opciones.clear()
    opciones = list(map(eliminarSaltoLinea, lineas))
    return tuple(opciones)

def validarPosesionVehiculo(poseeVehiculo: str):
    return True if poseeVehiculo == "SI" else False

def validarDocumento(nroDocumento: str):
    return True if ((nroDocumento.isnumeric()) and (len(nroDocumento) >= 7) and (len(nroDocumento) <= 8)) else False

def vehiculoExistente(nroPatente, archivo = open("Vehiculo.txt", "r", encoding= "utf-8")):
    """
    Verifica la existencia del vehiculo filtrando por patente
    """
    return True if (len(list(filter(lambda linea : linea.split(",")[0] == nroPatente, archivo.readlines())))) != 0 else False and archivo.close()

def habitacionOcupada(nroHabitacion: str, archivo = open("RegistroEstadia.txt", "r", encoding = "utf-8")):
    """
    Verifica si la habitación seleccionada se encuentra en uso o disponible
    """
    return True if len(list(filter(lambda linea : linea.split(",")[1] == nroHabitacion, archivo.readlines()))) != 0 else False and archivo.close()

def clienteExistente(nroDocumento: str, archivo = open("Cliente.txt", "r", encoding = "utf-8")):
    """
    Verifica la existencia del cliente filtrando por documento
    Parametros(nroDocumento -> numero de documento del cliente | archivo -> archivo que lee)
    """
    return True if len(list(filter((lambda linea : linea.split(",")[0] == nroDocumento), archivo.readlines()))) != 0 else False and archivo.close()