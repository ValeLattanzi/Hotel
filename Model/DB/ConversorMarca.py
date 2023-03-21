import sqlite3

from Model.Marca import Marca

class ConversorMarca:

    conexion : sqlite3.Connection

    def __init__(self):
        self.conexion = sqlite3.connect("C:\\Users\\Valentino\\Documents\\Universidad\\Paradigma\\Hotel\\Hotel.db")

    def crearTabla(self):
        cursor = self.conexion.cursor()
        cursor.execute("""
CREATE TABLE Marca (
	mar_codigo INT PRIMARY KEY,
	mar_nombre  VARCHAR(50)
);
        """)
        self.conexion.commit()

    def obtenerSiguiente_ID(self):
        cursor = self.conexion.cursor()
        consulta = f"SELECT * FROM Marca ORDER BY mar_codigo DESC LIMIT 1"
        cursor.execute(consulta)
        ultimo_registro = cursor.fetchone()
        if ultimo_registro is None:
            return 1
        else:
            return ultimo_registro[0] + 1

    def insertar_objeto(self, objeto : Marca):
        self.conexion.execute(f"INSERT INTO Marca (mar_codigo, mar_nombre) VALUES (?, ?)", tuple((self.obtenerSiguiente_ID(), objeto.Nombre)))
        self.conexion.commit()
    
    def getObjetos(self, query : str = ""):
        cursor = self.conexion.cursor()
        cursor.execute(f"SELECT * FROM Marca")
        registros = cursor.fetchall()
        return registros