#funciones anidadas

def calculadora(a, b, operacion='sumar'):
    # definimos función anidada
    def sumar(a, b):
        return a + b
    def restar(a, b):
        return a - b

    #llamamos a la función anidada
    if operacion == 'sumar':
        print(f'Resultado de sumar:  {sumar(a, b)}')
    elif operacion == 'restar':
        print(f'Resultado restar: {restar(a, b)}')

calculadora(5, 6)
calculadora(4, 3, operacion='restar')