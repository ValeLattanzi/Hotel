class Habitacion:

    def __init__(self):
        self._numero = 0

    #region Atributos
    _numero : int
    #endregion

    #region Responsabilidades

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero: int):
        self._numero = numero

    #endregion