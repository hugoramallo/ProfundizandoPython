#desempaquetar

numeros = [1,2,3]
print(numeros)
#elementos desempaquetados (sin corchetes), elegimos poner guiones
print(*numeros, sep='-')

#se puede aplicar a cualquier iterable (lista, tupla) con diccionarios **kwargs
#si en los parámetros usamos *args, se convertirían en una tupla y habría que iterarlos
def sumar(a, b, c):
    print(f'Resultado: {a + b+ c}')
#usamos operador unpacking *, así pasamos los 3 valores de la lista, 1, 2, 3
sumar(*numeros)

# extraer algunas partes de una lista o cualquier iterable
mi_lista = [1,2,3,4,5,6]
#desempaquetamos con *, b tomaría el resto de elmentos, excepto los dos últimos que serían para c y d
a, *b, c, d = mi_lista
print(mi_lista)

#usar para unir listas
lista1 = [1,2,3]
lista2 = [4,5,6]
#lista de listas
lista3 = [lista1, lista2]
print(f'Lista de listas: {lista3}')
#desempaquetamos
lista3 = [*lista1, *lista2]
print(f'Unir listas: {lista3}')

#diccionarios
dic1 = {'A':1, 'B':2, 'C':3}
dic2 = {'D':4, 'E':5}
#unimos diccionarios
dic3 = {**dic1, **dic2}
print(dic3)

#construir lista a partir de string, al utilizar el unpacking separa la palabra en letras en una lista
lista = [*'HolaMundo']
print(*lista, sep=' ')