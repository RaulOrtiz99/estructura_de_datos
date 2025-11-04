from nodo import Nodo


class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izquierdo, valor)
        else:
            if nodo.derecho is None:
                nodo.derecho = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.derecho, valor)

    def construir_desde_lista(self, valores):
        if not valores:
            return
        self.raiz = self._construir_recursivo(valores, 0)

    def _construir_recursivo(self, valores, indice):
        if indice >= len(valores) or valores[indice] is None:
            return None

        nodo = Nodo(valores[indice])
        nodo.izquierdo = self._construir_recursivo(valores, 2 * indice + 1)
        nodo.derecho = self._construir_recursivo(valores, 2 * indice + 2)

        return nodo

    def es_espejo(self, altura=None):
        if self.raiz is None:
            return True

        return self._es_espejo_recursivo(
            self.raiz.izquierdo, self.raiz.derecho, altura, 1
        )

    def _es_espejo_recursivo(self, izq, der, altura_max, altura_actual):
        if altura_max is not None and altura_actual > altura_max:
            return True

        if izq is None and der is None:
            return True

        if izq is None or der is None:
            return False

        return self._es_espejo_recursivo(
            izq.izquierdo, der.derecho, altura_max, altura_actual + 1
        ) and self._es_espejo_recursivo(
            izq.derecho, der.izquierdo, altura_max, altura_actual + 1
        )

    def obtener_altura(self):
        return self._calcular_altura(self.raiz)

    def _calcular_altura(self, nodo):
        if nodo is None:
            return 0

        altura_izq = self._calcular_altura(nodo.izquierdo)
        altura_der = self._calcular_altura(nodo.derecho)

        return 1 + max(altura_izq, altura_der)

    def imprimir(self):
        if self.raiz is None:
            print("Árbol vacío")
            return

        print("\nEstructura del árbol:")
        self._imprimir_recursivo(self.raiz, "", True)

    def _imprimir_recursivo(self, nodo, prefijo, es_derecho):
        if nodo is not None:
            print(prefijo + ("|-- " if es_derecho else "`-- ") + str(nodo.valor))

            if nodo.izquierdo is not None or nodo.derecho is not None:
                if nodo.izquierdo:
                    self._imprimir_recursivo(
                        nodo.izquierdo,
                        prefijo + ("|   " if es_derecho else "    "),
                        False,
                    )
                else:
                    print(prefijo + ("|   " if es_derecho else "    ") + "`-- None")

                if nodo.derecho:
                    self._imprimir_recursivo(
                        nodo.derecho, prefijo + ("|   " if es_derecho else "    "), True
                    )
                else:
                    print(prefijo + ("|   " if es_derecho else "    ") + "|-- None")
