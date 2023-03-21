import sqlite3
from Model.Pension import Pension

class ConversorPension:

    conexion : sqlite3.Connection

    def __init__(self):
        self.conexion = sqlite3.connect("C:\\Users\\Valentino\\Documents\\Universidad\\Paradigma\\Hotel\\Hotel.db")

    def crearTabla(self):
        cursor = self.conexion.cursor()
        cursor.execute("""
CREATE TABLE Pension (
	pen_codigo INT PRIMARY KEY,
	pen_nombre VARCHAR(50) NOT NULL,
	pen_precio DECIMAL(2,2) NOT NULL
);
        """)
        self.conexion.commit()

    def obtenerSiguiente_ID(self):
        cursor = self.conexion.cursor()
        consulta = f"SELECT * FROM Pension ORDER BY pen_codigo DESC LIMIT 1"
        cursor.execute(consulta)
        ultimo_registro = cursor.fetchone()
        if ultimo_registro is None:
            return 1
        else:
            return ultimo_registro[0] + 1
        
    def insertar_objeto(self, objeto : Pension):
        datosInsert = tuple((self.obtenerSiguiente_ID(), objeto.nombre, objeto.precio[:-1]))
        self.conexion.execute(f"INSERT INTO Pension (pen_codigo, pen_nombre, pen_precio) VALUES (?, ?, ?)", datosInsert)
        self.conexion.commit()
    
    def getObjetos(self, query : str = ""):
        cursor = self.conexion.cursor()
        cursor.execute(f"SELECT * FROM Pension")
        registros = cursor.fetchall()
        return registros