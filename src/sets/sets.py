#Los sets son colecciones no ordenadas de elementos unicos

mi_conjunto = {1,2,3,4,5}

otro_conjunto = {1,1,2,3,3,4,5,6}
print('en los conjuntos no se pueden repetir elementos')
print(otro_conjunto)

#metodos para agregar y eliminar elementos

# Añadir y eliminar elementos
mi_conjunto.add(6)  # Añade un elemento
mi_conjunto.remove(3)  # Elimina un elemento (lanza error si no existe)
mi_conjunto.discard(10)  # Elimina un elemento si existe (no lanza error si no existe)

# Operaciones de conjuntos
conjunto_a = {1, 2, 3, 4}
conjunto_b = {3, 4, 5, 6}
union = conjunto_a | conjunto_b  # {1, 2, 3, 4, 5, 6}
interseccion = conjunto_a & conjunto_b  # {3, 4}
diferencia = conjunto_a - conjunto_b  # {1, 2}
diferencia_simetrica = conjunto_a ^ conjunto_b  # {1, 2, 5, 6}
