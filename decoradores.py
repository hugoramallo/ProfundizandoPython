#decorador recibe una función como parámetro y devuelve otra función como clousure
#se usa para extender funcionalidad
#1. Función decorador (a)
#2. Función a decorar (b)
#3. Función decorada (c)

#vamos a decorar la siguiente función
#recibimos com parámetro la función mostrar_mensaje
def funcion_decorador_a(funcion_a_decorar_b):
    def funcion_decorada_c(*args, **kwargs):
        #llamamos a la función a decorar_b
        print('Antes desde la función_decorada_c')
        resultado = funcion_a_decorar_b(*args, **kwargs)
        print('Despues desde la función_decorada_c')
        return resultado
    return funcion_decorada_c

"""@funcion_decorador_a
def mostrar_mensaje():
    print('Hola desde función mostrar mensaje')

mostrar_mensaje()

@funcion_decorador_a
def imprimir():
    print('Hola desde función imprimir')

imprimir()
"""
@funcion_decorador_a
def sumar(a, b):
    return a + b

resultado = sumar(5, 6)
print(f'Resultado de la suma es: {resultado}')

