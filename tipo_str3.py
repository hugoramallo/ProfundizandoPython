# más str

# formato a un str
nombre = 'Juan'
edad = 28
#el operador de %(tipo de dato) nos permite sustituir valores, %s es un string, %d un entero
mensaje_con_formato = 'Mi nombre es %s y tengo %d '%(nombre,edad) #indicamos cual van a ser la variables que irán en el %
print(mensaje_con_formato)

# lo vamos a hacer con una tupla desde el principio

persona = ('Karla', 'Gómez', 5000.00)
#mensaje_con_formato = 'Hola %s %s. Tu sueldo es %.2f'%persona
#print(mensaje_con_formato)

mensaje_con_formato = 'Hola %s %s. Tu sueldo es %.2f'
#también le podemos pasar la tupla en el propio print
print(mensaje_con_formato%persona)

#método format
nombre = 'Juan'
edad = 28
sueldo = 3000
# es lo mismo que con % pero usando el método format, las llaves es donde se posicionan nuestras variables
mensaje = 'Nombre {} Edad {} Sueldo {:.2f}'.format(nombre, edad, sueldo)
print(mensaje_con_formato)

#queremos el elemento 0
mensaje = 'Nombre {0} Edad {1} Sueldo {2:.2f}'.format(nombre, edad, sueldo) #lo mismo pero indicando la posición
print(mensaje)

mensaje = 'Sueldo {2:.2f} Edad {1} Nombre {0}'.format(nombre, edad, sueldo)
print(mensaje)
#también se puede hacer con letras
mensaje = 'Nombre {n} Edad {e} Sueldo {s:.2f}'.format(n=nombre, e=edad, s=sueldo)
print(mensaje)

#con un diccionario, seguimos indicando los placeholder {}
diccionario = {'nombre':'Ivan', 'edad':34, 'sueldo':8000.00}
mensaje = 'Nombre {dic[nombre]}, Edad {dic[edad]}, Sueldo {dic[sueldo]:.2f}'.format(dic=diccionario)
print(mensaje)
###########
nombre = 'Juan'
edad = 28
sueldo = 3000
#aquí usamos el proceso de interpolación, sin necesidad de usar format
mensaje = f'Nombre {nombre} Edad {edad} Sueldo {sueldo:.2f}'
print(mensaje)

# Método print usando el separador
#nombre, edad, sueldo es una tupla de valores
print(nombre, edad, sueldo, sep=', ')


