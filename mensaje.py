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