from arbol_binario import ArbolBinario


def main():
    arbol = ArbolBinario()

    while True:
        print("\n" + "=" * 50)
        print("VERIFICADOR DE ÁRBOL ESPEJO - ED2")
        print("=" * 50)
        print("1. Construir árbol espejo perfecto (ejemplo)")
        print("2. Construir árbol NO espejo (ejemplo)")
        print("3. Construir árbol manualmente")
        print("4. Verificar si es espejo (todo el árbol)")
        print("5. Verificar si es espejo hasta una altura")
        print("6. Mostrar altura del árbol")
        print("7. Imprimir árbol")
        print("8. Salir")
        print("=" * 50)

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            arbol = ArbolBinario()
            arbol.construir_desde_lista([1, 2, 2, 3, 4, 4, 3])
            print("✓ Árbol espejo perfecto construido")

        elif opcion == "2":
            arbol = ArbolBinario()
            arbol.construir_desde_lista([1, 2, 2, 3, 4, 3, 4])
            print("✓ Árbol NO espejo construido")

        elif opcion == "3":
            print("\nIngrese valores (separados por espacio):")
            print("Ejemplo: 5 3 7 2 4 6 8")
            valores = input("Valores: ").split()
            arbol = ArbolBinario()
            for valor in valores:
                try:
                    arbol.insertar(int(valor))
                except ValueError:
                    print(f"Error: '{valor}' no es válido")
            print("✓ Árbol construido")

        elif opcion == "4":
            if arbol.raiz is None:
                print("⚠ El árbol está vacío")
            else:
                resultado = arbol.es_espejo()
                if resultado:
                    print("✓ El árbol ES ESPEJO")
                else:
                    print("✗ El árbol NO ES ESPEJO")

        elif opcion == "5":
            if arbol.raiz is None:
                print("⚠ El árbol está vacío")
            else:
                try:
                    altura = int(input("Ingrese la altura: "))
                    resultado = arbol.es_espejo(altura)
                    if resultado:
                        print(f"✓ El árbol ES ESPEJO hasta la altura {altura}")
                    else:
                        print(f"✗ El árbol NO ES ESPEJO hasta la altura {altura}")
                except ValueError:
                    print("Error: Ingrese un número válido")

        elif opcion == "6":
            altura = arbol.obtener_altura()
            print(f"\nAltura del árbol: {altura}")

        elif opcion == "7":
            arbol.imprimir()

        elif opcion == "8":
            print("\n¡Buena suerte en tu examen! 🎓")
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()
