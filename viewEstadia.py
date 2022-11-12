# Pantalla para el registro de estadias

from datetime import datetime
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
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
entryHabitacion = ttk.Combobox(ventana, values = consultarHabitaciones())
entryHabitacion.place(x = 90, y =  40)
entryHabitacion['values'] = ('101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '201', '202', '203', '204', '205', '206', '207', '208', '209', '210', '301', '302', '303', '304', '305', '306', '307', '308', '309', '310')

lblPension = Label(ventana, text = "Pension:", background="light blue").place(x = 235 , y = 40 )
entryPension = ttk.Combobox(ventana)
entryPension['values'] = ('Desayuno', 'Media Pension', 'Pension Completa')
entryPension.place(x = 280,y = 40)

lblFechaLimite = Label(ventana, text = "Fecha Límite:", background="light blue").place(x = 20,y = 70)
entryFechaLimite = Entry(ventana)
entryFechaLimite.place(x = 100, y = 70)

lblAcompañantes = Label(ventana, text="Acompañantes:", background="light blue").place(x = 250, y = 70)
entryAcompañantes = Entry(ventana)
entryAcompañantes.place(x = 340, y = 70)

lblPrecio =  Label(ventana, text = "Precio:", background="light blue").place(x = 425 , y = 40 )
entryPrecio = Entry(ventana)
entryPrecio.insert(0, "1500")
entryPrecio.place(x = 465,y = 40)
entryPrecio.config(state="disabled")

# GroupBox Cliente
lblNombreYApellido = Label(ventana, text = "Nombre y Apellido:", background="light blue").place(x = 20, y = 120 )
entryNombreYApellido = Entry(ventana)
entryNombreYApellido.place(x = 135, y = 120)

lblTipoDocumento = Label(ventana, text = "Tipo de Documento:", background="light blue").place(x = 15, y = 150)
entryTipoDocumento = Combobox(ventana,  state = "readonly")
entryTipoDocumento.place(x = 135, y = 150)
entryTipoDocumento['values'] = ('DNI', 'Pasaporte', 'Libreta Civica', 'Libreta Enrolamiento')

lblNumeroDocumento = Label(ventana, text="Nro Documento:", background="light blue").place(x = 280, y = 150)
entryNumeroDocumento = Entry(ventana)
entryNumeroDocumento.place(x = 380,y = 150)

lblPais = Label(ventana, text="Pais Origen:", background="light blue").place(x = 60,y = 180)
entryPais = Entry(ventana)
entryPais.place(x = 135, y = 180)

lblMail = Label(ventana, text = "Mail:", background="light blue").place(x = 345, y = 180)
entryMail = Entry(ventana)
entryMail.place(x = 380, y = 180)

lblPoseeVehiculo = Label(ventana, text = "Posee Vehículo:", background="light blue").place(x = 40, y = 210)
entryPoseeVehiculo = Combobox(ventana, values = ["SI", "NO"],  state = "readonly")
entryPoseeVehiculo.place(x = 135, y = 210)
# GroupBox Vehiculo
lblMarca = Label(ventana, text = "Marca:", background="light blue").place(x = 20 ,y = 280)
entryMarca = Combobox(ventana, values = consultarMarcas(),  state = "readonly")
entryMarca.place(x = 80, y = 280)
entryMarca['value'] = ('Abarth', 'Alfa Romeo', 'Aston Martin', 'Audi', 'Bentley', 'BMW', 'Cadillac', 'Caterham', 'Chevrolet', 'Citroen', 'Dacia', 'Ferrari', 'Fiat', 'Ford', 'Honda', 'Infiniti', 'Isuzu', 'Iveco', 'Jaguar', 'Jeep', 'Kia', 'KTM', 'Lada', 'Lamborghini', 'Lancia', 'Land Rover', 'Lexus', 'Lotus', 'Maserati', 'Mazda', 'Mercedes-Benz', 'Mini', 'Mitsubishi', 'Morgan', 'Nissan', 'Opel', 'Peugeot', 'Piaggio', 'Porsche', 'Renault', 'Rolls-Royce', 'Seat', 'Skoda', 'Smart', 'SsangYong', 'Subaru', 'Suzuki', 'Tata', 'Tesla', 'Toyota', 'Volkswagen', 'Volv')

lblPatente = Label(ventana,text = "Patente:", background="light blue").place(x = 240, y = 280)
entryPatente = tk.Entry(ventana)
entryPatente.place(x = 290, y = 280)
# GroupBox Botones

btnRegistrar = tk.Button(ventana, text = "REGISTRAR", bg="green", command = lambda: registrarEstadia(entryFechaActual.get(), entryHabitacion.get(), entryPension.get(), entryFechaLimite.get(), entryAcompañantes.get(), entryPrecio.get(), entryNumeroDocumento.get(), entryNombreYApellido.get(), entryTipoDocumento.get(), entryPais.get(), entryMail.get(), entryPoseeVehiculo.get(), entryPatente.get(), entryMarca.get()))
btnRegistrar.place(x = 100, y = 340)
btnCancelar =  tk.Button(ventana, text = "CANCELAR", bg="red", command = lambda: exit())
btnCancelar.place(x = 220, y = 340)

# separador = Separator(ventana, orient='horizontal')

ventana.mainloop()