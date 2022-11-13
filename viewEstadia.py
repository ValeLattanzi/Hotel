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
ventana.geometry("610x400")
ventana.title("Estadia")
ventana.maxsize(width = 610,height=400)
ventana.config(background="light grey")
# Genera el entry de la fecha actual la carga
entryFechaActual = Entry(ventana)
entryFechaActual.place(x = 20, y = 5)
entryFechaActual.insert(0, datetime.now().strftime("%d/%m/%Y")) #Ingreso la fecha en el entry
entryFechaActual.config(state = "disabled")

# Genera el grupo de los datos correspondientes a la habitacion
# region GroupBox Habitacion
frHabitacion = ttk.Labelframe(ventana, text="Habitacion")
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
# endregion

# Crea el grupo de los datos que son referidos al cliente
# region GroupBox Cliente
frCliente = Labelframe(ventana, text="Cliente")
frCliente.config(width=585, height= 200)
frCliente.place(x = 10, y = 115 )

lblNombreYApellido = Label(frCliente, text = "Nombre y Apellido:").place(x = 20, y = 0 )
entryNombreYApellido = Entry(frCliente)
entryNombreYApellido.place(x = 135, y = 0)

lblTipoDocumento = Label(frCliente, text = "Tipo de Documento:").place(x = 15, y = 25)
entryTipoDocumento = Combobox(frCliente,  state = "readonly")
entryTipoDocumento.place(x = 135, y = 25)
entryTipoDocumento['values'] = ('DNI', 'Pasaporte', 'Libreta Civica', 'Libreta Enrolamiento')

lblNumeroDocumento = Label(frCliente, text="Nro Documento:").place(x = 280, y = 25)
entryNumeroDocumento = Entry(frCliente)
entryNumeroDocumento.place(x = 380,y = 25)

lblPais = Label(frCliente, text="Pais Origen:").place(x = 60,y = 50)
entryPais = Entry(frCliente)
entryPais.place(x = 135, y = 50)
lblMail = Label(frCliente, text = "Mail:").place(x = 345, y = 50)
entryMail = Entry(frCliente)
entryMail.place(x = 380, y = 50)

lblPoseeVehiculo = Label(frCliente, text = "Posee Vehículo:").place(x = 40, y = 80)
entryPoseeVehiculo = Combobox(frCliente, values = ["SI", "NO"],  state = "readonly")
entryPoseeVehiculo.place(x = 135, y = 80)
# endregion

# Crea el grupo de los datos correspondientes al vehiculo
# region GroupBox Vehiculo
frVehiculo = Labelframe(frCliente, text="Vehiculo")
frVehiculo.config(width=565, height=60)
frVehiculo.place(x = 10, y = 110)

lblMarca = Label(frVehiculo, text = "Marca:").place(x = 20 ,y = 10)
entryMarca = Combobox(frVehiculo,  state = "readonly")
entryMarca.place(x = 80, y = 10)
entryMarca['value'] = ('Abarth', 'Alfa Romeo', 'Aston Martin', 'Audi', 'Bentley', 'BMW', 'Cadillac', 'Caterham', 'Chevrolet', 'Citroen', 'Dacia', 'Ferrari', 'Fiat', 'Ford', 'Honda', 'Infiniti', 'Isuzu', 'Iveco', 'Jaguar', 'Jeep', 'Kia', 'KTM', 'Lada', 'Lamborghini', 'Lancia', 'Land Rover', 'Lexus', 'Lotus', 'Maserati', 'Mazda', 'Mercedes-Benz', 'Mini', 'Mitsubishi', 'Morgan', 'Nissan', 'Opel', 'Peugeot', 'Piaggio', 'Porsche', 'Renault', 'Rolls-Royce', 'Seat', 'Skoda', 'Smart', 'SsangYong', 'Subaru', 'Suzuki', 'Tata', 'Tesla', 'Toyota', 'Volkswagen', 'Volv')

lblPatente = Label(frVehiculo, text = "Patente:").place(x = 240, y = 10)
entryPatente = tk.Entry(frVehiculo)
entryPatente.place(x = 300, y = 10)
# endregion

# Crea el grupo de los botones para las acciones permitidas para la pantalla
# region GroupBox Botones
frButtons = Labelframe(ventana)
frButtons.config(width=585, height=70)
frButtons.place(x = 10, y = 320)

btnRegistrar = tk.Button(frButtons, text = "REGISTRAR", bg="light green", command = lambda: registrarEstadia(entryFechaActual.get(), entryHabitacion.get(), entryPension.get(), entryFechaLimite.get(), entryAcompañantes.get(), entryPrecio.get(), entryNumeroDocumento.get(), entryNombreYApellido.get(), entryTipoDocumento.get(), entryPais.get(), entryMail.get(), entryPoseeVehiculo.get(), entryPatente.get(), entryMarca.get()))
btnRegistrar.place(x = 50, y = 10)
btnCancelar =  tk.Button(frButtons, text = "CANCELAR", bg="crimson", command = lambda: ventana.destroy())
btnCancelar.place(x = 450, y = 10)
# endregion
# separador = Separator(ventana, orient='horizontal')

ventana.mainloop()