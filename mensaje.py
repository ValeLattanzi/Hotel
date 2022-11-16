from tkinter import *
from tkinter import messagebox

def mensaje(mensaje: str, titulo: str):
    """
    Se crea una ventana emergente que muestra el texto que se recibe por parametros
    """
    if titulo == "ERROR":
        messagebox.showerror(title=titulo, message=mensaje)
    else:
        messagebox.showinfo(title=titulo, message=mensaje)
    # ventana = Tk()
    # ventana.title("Mensaje")
    # ventana.geometry("250x150")

    # lblMensaje = Label(ventana, text=mensaje)
    # lblMensaje.pack()

    # btnAceptar = Button(ventana, text="OK", background="light blue", command=lambda: ventana.destroy())
    # btnAceptar.pack()

    # ventana.mainloop()