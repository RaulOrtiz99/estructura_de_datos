#Ejercicios para practicar 

milista = [1,2,3,4,5,6,7,8,9,10] 

def par(n):
    return n % 2 == 0 

def partlista(milista):
    impares = [] 
    for numero in milista:
        if not par(numero):
            impares.append(numero)
    impares_ordenados = sorted(impares,reverse=True)

    return tuple(impares_ordenados)    


resultado = partlista(milista) 
print(resultado)

print("EJERCICIO 2====") 

inventario = {
    'manzanas': 430, 
    'bananas': 312, 
    'naranjas': 525, 
    'peras': 217
}


def producto_mas_caro(inventario):
    producto_caro = None 
    precio_maximo = float('-inf') 

    for producto, precio in inventario.items():
        if precio > precio_maximo:
            precio_maximo = precio 
            producto_caro = producto
    return producto_caro, precio_maximo 


producto, precio= producto_mas_caro(inventario)
print(f"el producto mas caro es",producto, precio)