# Unpacking o desempaquetado
valores = 1,2,3 #tupla
print(valores)
print(type(valores))

#definimos de golpe 3 variables
valor1, valor2, valor3 = 1, 2 ,3

print(valor1, valor2, valor3)

#omitir segundo valor, con _ se crea una variable que no vamos a usar
#el 2 (segundo valor) se asignará a la variable _ que no vamos a usar
valor1, _, valor3 = 1, 2, 3
print(valor1, _, valor3)

#asignar un número a valor 1, otro a valor 2 y el resto a valor 3 usando *
#se convierte el valor 3 en una lista
#las variables valor4 y valor5, se les asignará los dos últimos números
valor1, valor2, *valor3, valor4, valor5 = 1, 2, 3, 4, 5, 6, 7, 8, 9
print(valor1, valor2, valor3, valor4, valor5)

#ahora con una lista
valor1, valor2, *valor3, valor4, valor5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(valor1, valor2, valor3, valor4, valor5)
print(type(valor3))

def regresa_varios_datos():
    return 1, 2, 3

#asigna los valores que devuelve la función
valor1, valor2, valor3 = regresa_varios_datos()
print(valor1, valor2, valor3)

#con _ para no procesar los valores
valor1, *_ = regresa_varios_datos()
#primer valor
print(valor1)
#valores restantes
print(_)

#help(str.partition())
hora, separador, minutos = '17:20'.partition(':')
#print(type(variable))
print(hora, separador, minutos)
