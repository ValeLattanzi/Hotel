class Pension:

    def __init__(self):
        self._codigo = 0
        self._nombre = ""
        self._precio = 0
    
    def __init__(self, nombre : str, precio : int):
        self._codigo = 0
        self._nombre = nombre
        self._precio = precio

    #region Atributos
    _codigo : int
    _nombre : str
    _precio : str
    #endregion

    #region Responsabilidades
    @property
    def codigo(self):
        return self._codigo
    
    @codigo.setter
    def codigo(self, codigo: str):
        self._codigo = codigo
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre: str):
        self._nombre = nombre

    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self, precio: int):
        self._precio = precio
    #endregion