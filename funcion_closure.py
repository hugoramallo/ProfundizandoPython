#Un closure es una función que defina a otra y además la puede devolver
#La función anidada puede acceder a las variables locales definidas
#en la función principal o externa

#función principal
def operacion(a, b):
    # Definimos una función interna o anidada
    def sumar():
        #usamos las variables definidas en operación
        return a + b
    #retornar la función, sin paréntesis para no llamarla
    return sumar

# función lambda con closure
def operacion2(a, b):
    #definimos el lambda interno o anidado, usamos return para devovlerla
    return lambda: a + b

mi_funcion_closure = operacion(5, 2)
mi_funcion_closure2 = operacion(5, 2)
print(f'Resultado de la función closure: {mi_funcion_closure()}')
print(f'Resultado de la función closure: {mi_funcion_closure2()}')

#llamar la función regresada al vuelo, importante los paréntesis después para ejecutar la anidada
print(f'Resultado de la función closure al vuelo: {operacion(2, 3)()}')
print(f'Resultado de la función closure al vuelo: {operacion2(2, 3)()}')

