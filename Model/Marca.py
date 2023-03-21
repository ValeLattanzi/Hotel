class Marca:

    def __init__(self):
        self._codigo = 0
        self._nombre = ""

    def __init__(self, nombre: str):
        self._codigo = 0
        self._nombre = nombre
    
    #region Atributos
    _codigo : str
    _nombre : str
    #endregion

    #region Responsabilidades
    @property
    def codigo(self):
        return self._codigo
    @codigo.setter
    def codigo(self, codigo: str):
        self._codigo = codigo

    @property
    def Nombre(self):
        return self._nombre
    @Nombre.setter
    def Nombre(self, nombre: str):
        self._nombre = nombre
    #endregion