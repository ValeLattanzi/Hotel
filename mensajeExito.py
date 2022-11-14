from tkinter import *

def mensaje(mensaje: str):
    """
    Se crea una ventana emergente que muestra el texto que se recibe por parametros
    """
    ventana = Tk()
    ventana.title("Mensaje")
    ventana.geometry("250x150")

    lblMensaje = Label(ventana, text=mensaje)
    lblMensaje.pack()

    btnAceptar = Button(ventana, text="OK", background="light blue", command=lambda: ventana.destroy())
    btnAceptar.pack()

    ventana.mainloop()