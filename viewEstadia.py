# Pantalla para el registro de estadias

from datetime import datetime
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.ttk import *
from Estadia import registrarEstadia
from Estadia import calcularPrecioEstadia
# Crea la ventana
ventana = Tk()
ventana.geometry("600x400")
ventana.title("Estadia")
ventana.maxsize(width = 600,height=400)
ventana.config(background="light blue")

entryFechaActual = Entry(ventana)
entryFechaActual.place(x = 20, y = 5)
entryFechaActual.insert(0, datetime.now().strftime("%d/%m/%Y")) #Ingreso la fecha en el entry
entryFechaActual.config(state = "disabled")

# GroupBox Habitacion
frHabitacion = ttk.Labelframe(ventana, text="Habitacion")
style = ttk.Style()
style.configure(
    "TLabelFrame",
    foreground = "red",
    padding = [5,5,5,5]
)
frHabitacion.config(width=585, height=80)
frHabitacion.place(x=10, y=28)

lblHabitacion = Label(frHabitacion, text="Habitacion:").place(x = 10,y = 0)
entryHabitacion = ttk.Combobox(frHabitacion, state='readonly')
entryHabitacion.place(x = 75, y =  0)
entryHabitacion['values'] = ('101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '201', '202', '203', '204', '205', '206', '207', '208', '209', '210', '301', '302', '303', '304', '305', '306', '307', '308', '309', '310')

lblPension = Label(frHabitacion, text = "Pension:").place(x = 220 , y = 0)
entryPension = ttk.Combobox(frHabitacion, state='readonly')
entryPension['values'] = ('Desayuno', 'Media Pension', 'Pension Completa')
entryPension.place(x = 270,y = 0)

def pensionSeleccionada(event):
    btnInsertarPrecio = Button(frHabitacion, command= calcularPrecioEstadia(entryPension.get(), entryPrecio))

lblFechaLimite = Label(frHabitacion, text = "Fecha Límite:").place(x = 10,y = 25)
entryFechaLimite = Entry(frHabitacion)
entryFechaLimite.place(x = 90, y = 25)

lblAcompañantes = Label(frHabitacion, text="Acompañantes:").place(x = 240, y = 25)
entryAcompañantes = Entry(frHabitacion)
entryAcompañantes.place(x = 330, y = 25)

lblPrecio =  Label(frHabitacion, text = "Precio:").place(x = 415 , y = 0)
entryPrecio = Entry(frHabitacion)
entryPrecio.place(x = 455,y = 0)
entryPrecio.config(state="disabled")

entryPension.bind("<<ComboboxSelected>>", pensionSeleccionada)

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
entryMarca = Combobox(ventana,  state = "readonly")
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