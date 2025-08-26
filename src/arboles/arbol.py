from .nodo import Nodo

class Arbol:

    def __init__(self):
        self._raiz = None

    def get_raiz(self):
        return self._raiz

    def set_raiz(self, nodo):
        if nodo is not None and not isinstance(nodo, Nodo):
            raise TypeError("La raiz debe ser una instancia de Nodo o None")
        self._raiz = nodo

    #Metodos del arbol

    def es_vacio(self):
        return self._raiz is None
