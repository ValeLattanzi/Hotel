from Model.DB.ConversorPension import ConversorPension
from Model.Marca import Marca
from Model.Pension import Pension

with open("Habitaciones.txt", "r") as file:
    habitacion = file.readlines()

conversor = ConversorHabitaciones()
try:
    for h in habitacion:
        objPension = Pension(h)
        conversor.insertar_objeto(objPension)
    conversor.conexion.close()
except:
    Exception