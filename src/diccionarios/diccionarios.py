#los diccionarios almacenan clave valor  

mi_diccionario = {'nombre':'Ana','Edad': 25, 'ciudad':'Madrid'}
print(mi_diccionario)   


nombre = mi_diccionario['nombre'] 
print('asi se accede a la clave de un diccionario')
print(nombre) 
ciudad = mi_diccionario['ciudad']
print(ciudad) 
edad = mi_diccionario.get('Edad')
#asi obtento la edad del usuario usadno el metodo get
print('asi se accede a la clave de un diccionario usando get')
print (edad)

#modificar un valor de un diccionario 
mi_diccionario['profesion'] = 'programador' 
print('diccionario agregando una nueva clave y un nuevo valor...') 
print(mi_diccionario)
mi_diccionario['Edad']= 20 
print('diccionario modificando un valor de una clave que ya existe...')
print(edad)
mi_diccionario.pop('profesion')