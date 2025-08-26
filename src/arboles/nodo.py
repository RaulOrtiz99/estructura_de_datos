class Nodo:
    def __init__(self,valor):
        self._valor = valor
        self._izquierda= None
        self._derecho= None


    def get_valor(self):
        return self._valor

    def get_izquierdo(self):
        return self._izquierda

    def get_derecho(self):
        return self._derecho

    def set_valor(self,valor):
        self._valor = valor

    def set_izquierdo(self,valor):
        self._izquierda = valor

    def set_derecho(self,valor):
        self._derecho = valor

    def __repr__(self):
        return f"Nodo({self._valor})"
