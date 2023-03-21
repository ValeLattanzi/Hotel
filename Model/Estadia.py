from datetime import datetime

from Model.Habitacion import Habitacion
from Model.Pension import Pension
from Model.Cliente import Cliente

class Estadia:

    def __init__(self):
        self._codigo = 0
        self._fecha_inicio = datetime()
        self._fecha_fin = datetime()
        self._acompanantes = 0
        self._total_estadia = 0

    def __init__(self, codigo, fecha_inicio, fecha_fin, acompanantes, total_estadia):
        self._codigo = codigo
        self._fecha_inicio = fecha_inicio
        self._fecha_fin = fecha_fin
        self._acompanantes = acompanantes
        self._total_estadia = total_estadia
    
    #region Atributos
    _codigo : int
    _fechaInicio : datetime
    _fechaFin : datetime
    _acompañantes : int
    _totalEstadia : float
    _cliente : Cliente
    _pension : Pension
    _habitacion : Habitacion
    #endregion

    #region Responsabilidades

    @property
    def codigo(self):
        return self._codigo
    @codigo.setter
    def codigo(self, value):
        self._codigo = value

    @property
    def fecha_inicio(self):
        return self._fecha_inicio
    @fecha_inicio.setter
    def fecha_inicio(self, value):
        self._fecha_inicio = value

    @property
    def fecha_fin(self):
        return self._fecha_fin
    @fecha_fin.setter
    def fecha_fin(self, value):
        self._fecha_fin = value

    @property
    def acompanantes(self):
        return self._acompanantes
    @acompanantes.setter
    def acompanantes(self, value):
        self._acompanantes = value

    @property
    def total_estadia(self):
        return self._total_estadia
    @total_estadia.setter
    def total_estadia(self, value):
        self._total_estadia = value

    @property
    def Cliente(self):
        return self._cliente
    @Cliente.setter
    def Cliente(self, value):
        self._cliente = value

    @property
    def Pension(self):
        return self._pension
    @Pension.setter
    def Pension(self, value):
        self._pension = value

    @property
    def Habitacion(self):
        return self._habitacion
    @Habitacion.setter
    def Habitacion(self, value):
        self._habitacion = value
    #endregion