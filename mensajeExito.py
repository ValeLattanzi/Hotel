from tkinter import *

def mensaje(mensaje: str):
    ventana = Tk()
    ventana.title("Mensaje")
    ventana.geometry("300x150")

    lblMensaje = Label(ventana, text=mensaje)
    lblMensaje.pack()

    btnAceptar = Button(ventana, text="OK", background="light blue", command=lambda: ventana.destroy())
    btnAceptar.pack()

    ventana.mainloop()