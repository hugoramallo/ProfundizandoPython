#profundizando en tuplas
import numpy as np

#declarar variables
a, b = 'Hola', 'Adios'
print(a, b)
#swap (intercambio)
a, b = b, a
print(a, b)

#regresar múltiples valores en una función
#devuelve el mínimo y el máximo de un valor de una lista
def minmax(elementos):
    return min(elementos), max(elementos)

min, max = minmax([1,2,3,4,5])
print(f'Valor min: {min}, Valor max: {max}')

#regresa la suma de una tupla
resultado = sum((1,2,3,4,5))
print(f'Resultado: {resultado}')

#parámetros indefinidos / ilimitados con *args
def sumar(*args):
    #con sum no hace falta recorrer los elementos de los iterables
    return sum(args)

resultado = sumar(1,2,3,4,5)
print(f'Resultado: {resultado}')


a = np.array([1,2,3,4])
print(a[[False, True, False, False]])

