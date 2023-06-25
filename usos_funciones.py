# las funciones en python son ciudadanas de primera clase
#first class citizens (podemos definirla en cualquier parte de nuestro código)
#además podemos pasar también una función como argumento o pasarla a una variable
#una función esn un objeto en python

#definimos la función
def sumar(a, b):
    return a + b

# 1. Asignar una función a una variable (no se usan paréntesis)
#vamos a asignar la referencia de la función a esa variable
mi_funcion = sumar #sin paréntesis para no llamar la función

#verificar tipo de variable
print(type(mi_funcion))

# Llamamos la función a través de la variable
resultado = mi_funcion(5, 8)

print(f'Resultado: {resultado}')

#2. Función como argumento (parámetro)
def operacion(a, b, sumar_arg):
    print(f'Resultado de sumar: {sumar_arg(a, b)}')

operacion(4, 5, sumar)

# Podemos retornar una función
def retornar_funcion():
    return sumar

mi_funcion_retornada = retornar_funcion()
print(f'Resultado función retornada: {mi_funcion_retornada(5,7)}')