# profundizando listas
# listas son mutables
nombres1 = ['Juan', 'Karla','Pedro']
#usando split, generamos una lista con cada elemento
nombres2 = 'Laura María Gonzalo Ernesto'.split()
print(nombres2)
# sumas listas
print(f'Sumar listas: {nombres1}1 +  {nombres2}')

# Extender una lista con otra lista
nombres1.extend(nombres2)
print(f'Extender la lista1 con la lista2: {nombres1}')

# lista números
numeros1 = [10, 40, 15, 4, 20, 90, 4]
# si está repetido el número solo devuelve el índice del primer elemento encontrado
#help(list.index)
#imprimimos el índice de un elemento (posición que ocupa)
print(f'Indice 4: {numeros1.index(4)}')

# invertir orden elementos lista
numeros1.reverse()
print(f'Lista invertida: {numeros1}')

# ordenar los elementos de una lista
numeros1.sort() #orden de menor a mayor
print(f'Lista ordenada: {numeros1}')
#descedente
numeros1.sort(reverse=True) #orden descendente
print(f'Lista ordenada inversa: {numeros1}')

#Obtener el valor min y max de una lista
print(f'Valor minimo: {min(numeros1)}')
#valor máximo
print(f'Valor minimo: {max(numeros1)}')

#copiar los elementos de una lista
numeros2 = numeros1.copy()
#help(list.copy)  #regresa copia no profunda de la lista
print(numeros1)
print(numeros2)
print(f'Misma referencia: {numeros1 is numeros2}') #False, no lo son, así que la copia está bien
print(f'Mismo contenido: {numeros1 == numeros2}') #Si, el contenido es el mismo

#Podemos usar el constructor de la lista
numeros2 = list(numeros1) #diferente en referencia pero igual en contenido
print(f'Misma referencia: {numeros1 is numeros2}') #False, no lo son, así que la copia está bien
print(f'Mismo contenido: {numeros1 == numeros2}') #Si, el contenido es el mismo

# slicing
numeros2 = numeros1[:] # con dos puntos recorremos nuestra lista de inicio a fin
print(f'Misma referencia: {numeros1 is numeros2}') #False, no lo son, así que la copia está bien
print(f'Mismo contenido: {numeros1 == numeros2}') #Si, el contenido es el mismo

# multiplicación listas (lista de listas)
lista_multiplicacion = 5*[[2,5]] #se repiten estos números 5 veces al ser una lista de listas
#los valores 2,5 son objetos en memoria y al multiplicarse por 5 son el mismo objeto en memoria
print(lista_multiplicacion)
#preguntamos si es la misma referencia en memoria
print(f'Misma referencia: {lista_multiplicacion[0] is lista_multiplicacion[1]}') #si
print(f'Misma contenido: {lista_multiplicacion[0] == lista_multiplicacion[1]}') #si

#agregamos un elemento a la lista
lista_multiplicacion[2].append(10) #se agrega 10 a todos los objetos de la lista
print(lista_multiplicacion)

# Lista de lista = Matriz, con diferentes tamaños de listas
matriz = [[10,20], [30,40,50], [60, 70, 80, 90]]
print(f'Matriz original: {matriz}')
#imprimimos un elemento en cuestión
print(f'Fila 0, Columna 0: {matriz[0][0]}')
#seleccionar el 80
print(f'Fila 0, Columna 0: {matriz[2][2]}')
#modificar elemento en matriz
matriz[2][0] = 65
print(f'Fila 0, Columna 0: {matriz[2][0]}')

#ordenar lista de listas = matriz
lista_listas = [[10,14,87,90,71],[4,5,6,7],[9,0,11,15,45,61,70]]
#ordenamos por la sublista con la menor cantidad de elementos y así progresivamente
lista_listas.sort(key=len) #ordenar por largo
print(f'Ordenar lista: {lista_listas}')

# sorted built-in
#help(sorted)
nombres1 = ['Juan Carlos', 'Karla', 'Pedro', 'Esperanza']
#ordenamos de manera ascendente y volvemos a reasignar el valor
nombres1 = sorted(nombres1)
print(nombres1)

#orden descendente
nombres1 = sorted(nombres1, reverse=True)
print(nombres1)

#ordenar por la cantidad de caracteres (largo)
nombres1 = sorted(nombres1, key=len)
print(nombres1)

#built-in reversed
nombres1 = reversed(nombres1)
print(nombres1) #imprime un iterador, o si itera o se hace un cast a una lista
print(list(nombres1))
