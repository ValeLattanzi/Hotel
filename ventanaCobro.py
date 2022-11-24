from datetime import datetime
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.ttk import *
from mensaje import mensaje
from Funciones import AbrirVentana

# region Funciones
#se busca el dni en el txt registrar estadia. 
def buscarDni(dni: str, lineas = open("RegistroEstadia.txt", "r").readlines() ):
    #recorre las lineas del archivo
    for i in lineas:
        if i.split(",")[6] == dni: #si en una linea, sencuentra el dni ingresado
            return True # se devuleve true

#se veridica el dni ingresado se encuentre registrado anteriormente
#si es asi, se muestran los datos en pantalla
#si no, se muestra un mensaje de error
def verificarDni(ventana, fecha):
    if( buscarDni(entryDNI.get())==True)  :
        mostrarDatos(entryDNI.get(), ventana, fecha) 
    else:
        mensaje("DNI no encontrado!","ERROR")

#funcion que busca un dato en el txt registrarEstadia, segun su posicion en la linea
#devolviendo el mismo
def devolverElemento(elemento: int ,dni: str, lineas = open("RegistroEstadia.txt", "r").readlines() ):
    #recorre las lineas del archivo
    for i in lineas:
        if i.split(",")[6] == dni:
            return (i.split(",")[elemento])


#funcion que habilita frame 2, donde se trae los datos de la estadia de un cliente
#se la llama con el botón "buscar", al ingresar el DNI
def mostrarDatos(nroDocumento, ventana, fecha):
    #mostar los datos en la ventana:
    #configurar dimensiones del frame 2
    frCobro2 = ttk.Labelframe(ventana, text="Cobro")
    frCobro2.config(width = 585, height = 130)
    frCobro2.place(x = 10, y = 120)
    #precio por dia, lo traemos mediante la funcion devolver elemento.
    lblPrecio = Label(frCobro2, text = "Precio por día:     $").place(x = 20,y = 15) 
    entryPrecio = Entry(frCobro2)
    entryPrecio.place(x = 120, y = 15)
    entryPrecio.insert(0, devolverElemento(5,nroDocumento))
    entryPrecio.config(state='readonly')
    
    #cantidad de dias, traido desde la funcion
    lblCantDias=Label(frCobro2, text= "Cantidad de días: ").place(x=20, y=40)
    entryCantDias=Entry(frCobro2)
    entryCantDias.place(x = 120, y = 40)
    entryCantDias.insert(0, devolverElemento(8,nroDocumento))
    entryCantDias.config(state='readonly')

    #desplegable de la forma de cobro:
    lblFormaCobro = Label(frCobro2, text = "Forma de cobro:").place(x=20, y=65)
    entryFormaCobro = Combobox(frCobro2, values = ["Efectivo", "Tarjeta de crédito int."],  state = "readonly")
    entryFormaCobro.place(x = 120, y = 65)

    #desplegable del tipo de moneda a cobrar:
    lblMoneda = Label(frCobro2, text = "Moneda:").place(x = 280, y = 15)
    entryMoneda = Combobox(frCobro2, values = ["Euro", "Dolar" , "Peso"])
    entryMoneda.place(x = 370, y = 15)

    #ingresar cotizacion del dia:
    lblCotizacion = Label(frCobro2, text = "Cotización: ").place(x = 280, y = 40) 
    entryCotizacion = Entry(frCobro2)
    entryCotizacion.place(x = 370, y = 40)

    
    #entryMoneda.bind("<<ComboboxSelected>>", setMoneda(entryMoneda.get(), entryCotizacion))

    #boton calcular, donde mediante lambda se llama a la función para verificar que los campos estan completos
    #si estan completos se muestra el frame 3
    btnCalcular= tk.Button(frCobro2, text = "Calcular", bg="light blue" ,command = lambda:(verificarCampos(entryCotizacion.get(), entryFormaCobro.get(), entryMoneda.get(), nroDocumento, ventana, fecha)))
    btnCalcular.place(x =500, y = 40 )

#frame 3, donde se encuentra el monto total a cobrar y se habilita el boton registrar cobro
def framenum3(fecha, dni:str,  cotizacion:int, formaCobro:str, moneda:int, ventana):
    #monto total:
    frCobro3 = ttk.Labelframe(ventana, text="Cotización")
    frCobro3.config(width = 585, height = 80)
    frCobro3.place(x = 10, y = 270)
    lblMontoTotal=Label(frCobro3, text= "Monto total:        $").place(x =20 ,y = 10)
    entryMontoTotal=Entry(frCobro3)
    entryMontoTotal.place(x = 60, y =10 )
    entryMontoTotal.insert(0, (calcularMontoTotal(dni)//float(cotizacion)))
    entryMontoTotal.config(state='readonly')

    #boton registrar cobro, donde se llama la funcion llamar funciones
    btnRegCobro= tk.Button(frCobro3, text = "Registrar cobro", bg="light blue" ,command = lambda:llamarFunciones(fecha,dni,formaCobro, moneda, cotizacion, entryMontoTotal.get()))
    btnRegCobro.place(x =240, y = 30 )

#una vez se registra el cobro, se elimina la linea del cliente en el txt registrar estadia
# se registran los datos en el txt de registroCobro, y se muestra el mensaje de éxito.
def llamarFunciones(fecha, dni,formaCobro, moneda, cotizacion, monto):
    eliminarLinea(dni)
    DatosCobro(fecha,dni,formaCobro, moneda, cotizacion, monto)
    mensaje("Cobro registrado con éxito!","ÉXITO")


#funcion para verificar si los campos del frame 2 estan llenos
#en el campo cotizacion se verifica que se haya ingresado un numero y no otra cosa
# si no es así, se manda un mensaje de error
def verificarCampos(cotizacion, formaCobro, moneda, dni:str, ventana, fecha):
    num="1234567890."
    bandera=0
    for i in range(0,len(cotizacion)):
        if cotizacion[i] not in num:
            bandera=1
    if bandera==1:
        mensaje("Campo de cotización incorrecto!","ERROR")
    else:
        if cotizacion!="" and moneda!="" and formaCobro!="":
            framenum3(fecha, dni,  cotizacion, formaCobro, moneda, ventana)

        else:
            mensaje("Campos obligatorios incompletos!","ERROR")

#se calcula el monto a cobrar en pesos, obteniendo el precio de la estadia y la cantidad de dias que se aloja el cliente, segun su dni
def calcularMontoTotal(dni:str,):
    return(float(devolverElemento(5,dni)) * int(devolverElemento(8,dni)))


#funcion para registrar una nueva linea en el txt registroCobro, generada por nuestra pantalla
def DatosCobro(fecha, dni:str,formaCobro:str, moneda:int, cotizacion:int, monto:int,archivo=open("RegistroCobro.txt","a")):
    archivo.write(fecha+","+dni+","+formaCobro+","+moneda+","+cotizacion+","+monto+"\n")
    archivo.close()


#abrimos el archivo en modo lectura, guardando las lineas en un vector
#abrimos en modo escritura para recorrer cada linea y, volviendo a escribir aquellas que no 
#contengan el dni del cliente que ya pago
def eliminarLinea(dni):
    f=open("RegistroEstadia.txt", "r")
    lines=f.readlines()
    f.close()

    f=open("RegistroEstadia.txt", "w")
    for i in lines:
        if not dni in i:
            f.write(i)

    f.close()
# endregion

# Creacion de la ventana 
ventana = Tk()
ventana.geometry("610x400")
ventana.title("Cobro")
ventana.maxsize(width = 610,height=400)
ventana.config(background="light grey")

# region GroupBox Cobro
frCobro = ttk.Labelframe(ventana, text="Cobro")
frCobro.config(width = 585, height = 80)
frCobro.place(x = 10, y = 30)

#Ingreso de datos por pantalla 
lblDNI = Label(frCobro, text = "DNI:").place(x = 10,y = 30) 
entryDNI = Entry(frCobro)
entryDNI.place(x = 50, y = 30)

#campo de la fecha actual
lblFecha = Label(frCobro, text = "Fecha").place(x = 10,y = 5) 
entryFechaActual = Entry(frCobro)
entryFechaActual.place(x = 50, y = 5)
entryFechaActual.insert(0, datetime.now().strftime("%d/%m/%Y")) #Ingreso la fecha en el entry
entryFechaActual.config(state = "disabled")

#boton que llama la funcion verificar dni, donde dependiente de la misma se mostraran o no 
#los demas campos de la pantalla
btnBuscar = tk.Button(frCobro, text = "BUSCAR", bg="light blue" ,command = lambda:verificarDni(ventana, entryFechaActual.get())) #llama a la funcion en el momento en que la presionas
btnBuscar.place(x =190, y = 28) #posicion del boton verde buscar 
# endregion

AbrirVentana(ventana)