from tkinter import *
from Funciones import AbrirVentana
from Funciones import CerrarVentana

def btnRegistrarEstadia_Click():
    from viewEstadia import ventana
    return AbrirVentana(ventana)

# region Ventana
ventana = Tk()
ventana.title("Hotel - Portal Del Sol")
ventana.geometry("400x310")
ventana.maxsize(height = 310, width=400)
ventana.minsize(height = 310, width=400)
ventana.config(background = "light grey")

# region frOpciones
frOpciones = LabelFrame(text = "Opciones:")
frOpciones.config(width = 380, height = 290)
frOpciones.place(x = 10, y = 10)

btnRegistrarEstadia = Button(frOpciones ,text = "Registrar Estadia", background = "light blue",
    command = lambda : btnRegistrarEstadia_Click())
btnRegistrarEstadia.place(x = 140, y = 20)

btnRegistrarCobro = Button(frOpciones, text = "Registrar Cobro", background = "light blue")
btnRegistrarCobro.place(x = 142, y = 50)
# endregion

imgLogo = PhotoImage(file = "image.png")
lblImage = Label(ventana, image = imgLogo)
lblImage.place(x = 40, y = 110)

AbrirVentana(ventana)
# endregion