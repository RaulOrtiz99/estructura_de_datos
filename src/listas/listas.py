# creacion de una lista
mi_lista = [1, 2,3,4, 5, 6]
print(mi_lista)

# Acceder a elementos indices de una lista (indice 0-based)

primer_elemento = mi_lista[0]
ultimo_elemento = mi_lista[-1]
print("Acceso a elementos de una lista...")
print("PRIMER ELEMENTO")
print(primer_elemento)
print("ULTIMO ELEMENTO")
print(ultimo_elemento)

# Modificar elementos
mi_lista[0] = 100
print("Modificacion de elementos de una lista...")
print(mi_lista)

# Metodos comunes
print("Metodo append...")
mi_lista.append(7)
print(mi_lista)
print("Metodo insert...")
mi_lista.insert(1,200)
print(mi_lista)
print("Metodo remove...")
mi_lista.remove(200)
print(mi_lista)
longitud = len(mi_lista)
print("Longitud de la lista...")
print(longitud)
