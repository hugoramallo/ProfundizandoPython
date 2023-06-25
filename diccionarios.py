#profundizando en diccionarios

#los dic guardan un orden (a diferencia de un set)
#los diccionarios son mutables pero las llaves son inmutables
diccionario = {'Nombre':'Juan','Apellido':'Perez','Edad':28}
print(diccionario)
#usando listas para la llave no funcionan por ser mutables
#pero usando tuplas si
diccionario = {(1,2):'Valor'}
print(diccionario)

#se agrega una llave si no se encuentra dentro
diccionario ['Departamento'] = 'Sistemas'
print(diccionario)

# no hay valores duplicados en las llaves de un diccionario, los valores si
#si ya existe se reemplaza
diccionario['nombre'] = 'Juan Carlos'
print(diccionario)

#recuperar elementos de un diccionario, indicando una llave
print(diccionario['nombre'])

# Si no encuentra la llave, lanzará una excepción
#print(diccionario['Nombre'])

# Método get recupera una llave, y sino existe No lanza excepción
#podemos agregar un valor en caso de que la llave no existe
print(diccionario.get('Nombre')) #None
print(diccionario.get('nombre'))

#método setdefault si modifica el diccionario en caso de que no se encuentre la llave
#además se puede agregar un valor por default
nombre = diccionario.setdefault('Nombre','Valor por default')
print(nombre)
print(diccionario)

#forma más simple de imprimir un diccionario con pprint
from pprint import pprint as pp
#help(pp)
#imprimimos y lo ordena de forma ascedente por defecto
#con sort_dicts establecemos el orden por el que fuimos agregando los elementos originalmente
pp(diccionario, sort_dicts=False)
