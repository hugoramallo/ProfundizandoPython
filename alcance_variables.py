# Alcance de variables (scope) tiempo de vida de una variable

var_global = 'Variable global'

def imprimir():
    #Acceder a una variable global
    global var_global #esta opcion no hace falta solo para leer, es por si queremos escribir en esa variable
    print(f'Variable global desde función: {var_global}')
    # Definición de variable local
    #las variables locales se destruyen al momento donde deja de ejecutarse el código donde fue definida
    #tabmién se puede usar dentro de funciones anidadas
    var_local = 'Variables local'
    print(f'Variable local desde función: {var_local}')
    var_global = 'Nuevo valor de la variable global'
    def funcion_anidada():
        print(f'Variable local dentro de la función anidada: {var_local}')
    funcion_anidada()

imprimir()
print(f'Var global fuera de la función {var_global}')
#no es posible acceder a variables locales fuera
#del bloque donde se definieron, pero si dentro de funciones anidadas de ese bloque


