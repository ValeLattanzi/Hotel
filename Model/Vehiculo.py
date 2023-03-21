from Model.Marca import Marca


class Vehiculo:

    def __init__(self):
        self._codigo = 0
        self._patente = ""
        self._marca = Marca()

    def __init__(self, patente: str, marca: Marca):
        self._codigo = 0
        self._patente = patente
        self._marca = marca

    #region Atributos
    _codigo : int
    _patente : str
    _marca : Marca
    #endregion

    #region Responsabilidades
    @property
    def codigo(self):
        return self._codigo
    
    @codigo.setter
    def codigo(self, codigo: str):
        self._codigo = codigo

    @property
    def patente(self):
        return self._patente
    
    @patente.setter
    def patente(self, patente: str):
        self._patente = patente

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca: Marca):
        self._marca = marca 

    def recuperarMarca(self):
        # Recupera la marca segun la seleccion del usuario en la pantalla
        return 0
    
    def buscarMarcas():
        # Recupera un listado de todas las marcas
        return 0
    
    def getObjMarca(self):
        # Con un objeto que conoce su codigo ya, lo recupera de la base de datos
        return 0
    #endregion