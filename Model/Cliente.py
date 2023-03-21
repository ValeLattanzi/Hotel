from Vehiculo import Vehiculo

class Cliente:

    def __init__(self):
        self._nombre = ""
        self._apellido = ""
        self._nroDocumento = ""
        self._vehiculo = []

    def __init__(self, nombre, apellido, numero_documento, vehiculos):
        self._nombre = nombre
        self._apellido = apellido
        self._nroDocumento = numero_documento
        self._vehiculo = vehiculos
    
    #region Atributos
    _nombre : str
    _apellido : str
    _nroDocumento : str
    _vehiculo : list[Vehiculo]
    #endregion

    #region Responsabilidades
    @property
    def Nombre(self):
        return self.nombre
    @Nombre.setter
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    @property
    def Apellido(self):
        return self.apellido
    @Apellido.setter
    def set_apellido(self, apellido):
        self.apellido = apellido
    
    @property
    def Nrodocumento(self):
        return self.numero_documento
    @Nrodocumento.setter
    def set_numero_documento(self, numero_documento):
        self.numero_documento = numero_documento
    
    @property
    def Vehiculos(self):
        return self._vehiculo
    @Vehiculos.setter
    def set_vehiculos_disponibles(self, vehiculos_disponibles):
        self._vehiculo = vehiculos_disponibles

    def buscarVehiculos(self):
        return 0
    
    def recuperarVehiculo(self):
        return 0
    
    def getObjVehiculo(self):
        return 0
    #endregion
