# region Imports
from tkinter import *
from Funciones import AbrirVentana
from Funciones import CerrarVentana
from PIL import Image, ImageTk
# endregion

# region Funciones
def btnRegistrarEstadia_Click():
    from viewEstadia import ventana
    return AbrirVentana(ventana)

def btnRegistrarCobro_Click():
    from ventanaCobro import ventana
    return AbrirVentana(ventana)
# endregion

# region Ventana
ventana = Tk()
ventana.title("Hotel - Portal Del Sol")
ventana.geometry("400x310")
ventana.maxsize(height = 310, width = 400)
ventana.minsize(height = 310, width = 400)
ventana.config(background = "white")

# region frOpciones
frOpciones = LabelFrame(text = "Opciones:")
frOpciones.config(width = 380, height = 100)
frOpciones.place(x = 10, y = 10)

btnRegistrarEstadia = Button(frOpciones ,text = "Registrar Estadia", background = "light blue",
    command = lambda : btnRegistrarEstadia_Click())
btnRegistrarEstadia.place(x = 140, y = 10)

btnRegistrarCobro = Button(frOpciones, text = "Registrar Cobro", background = "light blue", command = lambda : btnRegistrarCobro_Click())
btnRegistrarCobro.place(x = 142, y = 40)
# endregion

img = Image.open("imgWhats.png", mode = 'r')
resize_image = img.resize(size = (170, 190))
imgLogo = ImageTk.PhotoImage(resize_image)
lblImage = Label(ventana, image = imgLogo)
lblImage.image = imgLogo
lblImage.place(x = 110, y = 110)

AbrirVentana(ventana)
# endregion