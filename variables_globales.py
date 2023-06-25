#definimos variable global
contador = 0

def mostrar_contador():
    print(contador)



#para poder escribir en una variable global dentro de una función
#hace falta especificar global y el nombre de la variable dentro de esa función
def modificar_contador(c):
    global contador
    contador = c


modificar_contador(5)
mostrar_contador()