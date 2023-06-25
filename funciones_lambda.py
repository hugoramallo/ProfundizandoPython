# Función lambda
# Son funciones anónimas (no tienen nombre asignado) y son pequeñas

#comparamos una función normal

#a una función normal no se permite asignarla al crearla una variable directamente
def sumar(a, b):
    return a + b

#con una función lambda si podemos asignarla directamente al crearla a una vsariable
# los lambda son anónimos, sin nombre y una sola línea de código
# no se necesitan agregar paréntesis para los parámetros
# no se necesita usar return, pero si debe expresar una expresión
# solo puede contener una expresión
# así se define la misma función de sumar pero con un lambda
mi_funcion_lambda = lambda a, b: a + b
#ejecutar un lambda
resultado = mi_funcion_lambda(4,6)
print(f'Resultado de sumar con función lambda: {resultado}')

#función lambda que no recibe argumentos (debemos regresar una expresión válida)

mi_funcion_lambda = lambda: 'Función sin argumentos'
print(f'LLamar función lambda sin argumentos: {mi_funcion_lambda()}')

# función lambda con parámetros por default
mi_funcion_lambda = lambda a=2, b=3: a + b
print(f'Resultado argumentos por default: {mi_funcion_lambda()}')

# función lambda con argumentos variables *args y **kwargs
mi_funcion_lambda = lambda *args, **kwargs: len(args) + len(kwargs)
print(f'Resultado argumentos variables: {mi_funcion_lambda(1,2,3, a=5,b=6)}')

#funciones lambda con argumentos, argumentos variables y valores por default
mi_funcion_lambda = lambda a, b, c=3, *args, **kwargs: a+b+c+len(args)+len(kwargs)
print(f'Resultado función lambda: {mi_funcion_lambda(1,2,4, 5,6,7,e=5, f=7)}')