#unir uno o más iterables
#clases y métodos disponibles en python
#print(dir(__builtins__))
#help(zip)
#creamos una tupla y una lista, pero también puede ser lista y lista o tupla y tupla o mezcladas
numeros = (1,2,3)
letras = ['a','b','c','d']
#tupla como números enteros
identificadores = 321, 322, 323, 324, 325
#creamos un set
conjunto = {6, 4, 0, 9, 8, 15, 10}
#usamos la función zip para unir las dos listas en una
#al aplicar la función zip, solamente se van a tomar 3 números, 3 letras, 3 identificadores
#esto es debido a que la tupla más corta es de 3 valores
mezcla = zip(numeros, letras, identificadores, conjunto) #objeto de tipo zip
#imprimimos como lista
print(list(mezcla))
#así lo imprimimos como una tupla
print(tuple(zip(numeros, letras)))
#preguntamos tipo de la variable mezcla (zip)
print(type(mezcla))

#interar en paralelo
for numero, letra, id, aleatorio in zip(numeros, letras, identificadores, conjunto):
    print(f'Número: {numero}, Letra: {letra}. Id: {id}), Aleatorio: {aleatorio}')

nueva_lista = []

for numero, letra, id, aleatorio in zip(numeros, letras, identificadores, conjunto):
    nueva_lista.append(f'{id}-{numero}-{letra}-{aleatorio}')
print(nueva_lista)

#unzip (separar elementos de dos o mas iterables y a asignar a variables por separado)
mezcla = [(1,'a'),(2,'b'),(3,'c')]
#zip junta varios iterables,
numeros, letras = zip(*mezcla) #1,2,3 a números y a,b,c a letras
print(f'Numeros: {numeros}, Letras: {letras}')

#ordenamiento (solo se combinan la lista de los elementos con menos iterables/elementos)
letras = ['c','d','a','e','b']
numeros = [3,2,4,1,0]
mezcla = zip(letras, numeros)
#sin orden
print(tuple(mezcla))
#ordenar por letra (primer iterable)
#hay que volver a generar el zip
print(sorted(zip(numeros, letras)))

#crear un diccionario con zip a partir de dos iterables
llaves = ['Nombre','Apellido','Edad']
valores = ['Juan','Pérez',18]
diccionario = dict(zip(llaves, valores))
print(diccionario)

#actualizar un elemento de un diccionario (tiene que ser un iterable)
llave = ['Edad'] #si no se encuentra se agrega
nueva_edad = [28]
diccionario.update(zip(llave, nueva_edad))
print(diccionario)