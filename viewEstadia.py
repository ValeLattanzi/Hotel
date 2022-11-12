# Pantalla para el registro de estadias



from datetime import datetime
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from Estadia import registrarEstadia
from Estadia import consultarTipoDocumento
from Estadia import consultarMarcas
from Estadia import consultarHabitaciones
from Estadia import consultarPensiones
# Crea la ventana
ventana = Tk()
ventana.geometry("600x400")
ventana.title("Estadia")
ventana.maxsize(width = 600,height=400)
ventana.config(background="light blue")

entryFechaActual = Entry(ventana)
entryFechaActual.place(x = 20, y = 10)
entryFechaActual.insert(0, datetime.now().strftime("%d/%m/%Y")) #Ingreso la fecha en el entry
entryFechaActual.config(state = "disabled")

# GroupBox Habitacion
lblHabitacion = Label(ventana, text="Habitacion:", background="light blue").place(x = 20,y = 40)
entryHabitacion = Combobox(ventana, values = consultarHabitaciones()).place(x = 90, y =  40)

lblPension = Label(ventana, text = "Pension:", background="light blue").place(x = 220 , y = 40 )
entryPension = Combobox(ventana, values = consultarPensiones()).place(x = 280,y = 40)

lblFechaLimite = Label(ventana, text = "Fecha Límite:", background="light blue").place(x = 20,y = 70)
entryFechaLimite = Entry(ventana).place(x = 100, y = 70)

lblAcompañantes = Label(ventana, text="Acompañantes:", background="light blue").place(x = 250, y = 70)
entryAcompañantes = Entry(ventana).place(x = 340, y = 70)

lblPrecio =  Label(ventana, text = "Precio", background="light blue").place(x = 410 , y = 40 )
entryPrecio = Entry(ventana)
entryPrecio.insert(0, "1500")
entryPrecio.place(x = 450,y = 40)
entryPrecio.config(state="disabled")

# GroupBox Cliente
lblNombreYApellido = Label(ventana, text = "Nombre y Apellido:", background="light blue").place(x = 20, y = 120 )
entryNombreYApellido = Entry(ventana).place(x = 135, y = 120)

lblTipoDocumento = Label(ventana, text = "Tipo de Documento:", background="light blue").place(x = 15, y = 150)
entryTipoDocumento = Combobox(ventana, values = consultarTipoDocumento(),  state = "readonly")
entryTipoDocumento.place(x = 135, y = 150)

lblNumeroDocumento = Label(ventana, text="Nro Documento:", background="light blue").place(x = 280, y = 150)
entryNumeroDocumento = Entry(ventana).place(x = 380,y = 150)

lblPais = Label(ventana, text="Pais Origen:", background="light blue").place(x = 60,y = 180)
entryPais = Entry(ventana).place(x = 135, y = 180)

lblMail = Label(ventana, text = "Mail:", background="light blue").place(x = 345, y = 180)
entryMail = Entry(ventana).place(x = 380, y = 180)

lblPoseeVehiculo = Label(ventana, text = "Posee Vehículo:", background="light blue").place(x = 40, y = 210)
entryPoseeVehiculo = Combobox(ventana, values = ["SI", "NO"],  state = "readonly")
entryPoseeVehiculo.place(x = 135, y = 210)
# GroupBox Vehiculo
lblMarca = Label(ventana, text = "Marca:", background="light blue").place(x = 20 ,y = 280)
entryMarca = Combobox(ventana, values = consultarMarcas(),  state = "readonly").place(x = 80, y = 280)

lblPatente = Label(ventana,text = "Patente:", background="light blue").place(x = 240, y = 280)
entryPantente = Entry(ventana).place(x = 290, y = 280)
# GroupBox Botones

btnRegistrar = tk.Button(ventana, text = "REGISTRAR", bg="green", command = lambda: registrarEstadia(ventana)).place(x = 100, y = 340)
btnCancelar =  tk.Button(ventana, text = "CANCELAR", bg="red", command = lambda: exit()).place(x = 220, y = 340)

# separador = Separator(ventana, orient='horizontal')

ventana.mainloop()