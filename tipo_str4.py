from urllib.request import urlopen

palabras = []
#with urlopen('http://globalmentoring.com.mx/recursos/GlobalMentoring.txt') as mensaje:
   # contenido = mensaje.read().decode('utf-8')

#contar ocurrencias (palabras) de una cadena
#print('No. veces Universidad: ',contenido.count('Universidad'))

#convertir a mayúsculas un string
#los tipos str son inmutables
#print(contenido.upper())
#print(contenido)

#pasarlo a minusculas
#print(contenido.lower())

# buscar la palabra python en un contenido
#print('Existe python?:'.lower() in contenido.lower())
#print('Existe python?:'.upper() in contenido.upper())

# startswith - inicia con
#print(contenido.startswith('En globalmentoring.com.mx'))

# endswith - termina con
#print(contenido.endswith('globalmentoring.com.mx'))

# preguntar si una cadena todos sus caracteres en minúscula o manyúscula, convertimos a minuscula
mensaje = 'Hola Mundo'
print(mensaje.lower().islower())
#lo mismo en mayúscula convirtiendo a mayúscula
print(mensaje.upper().isupper())

#Alinear cadenas

#center
titulo = 'Sitio web de Globalmentoring.com.mx'
#comprobamos la longitud
#print(len(titulo))
#centramos con 50 caracteres 50, y el fillchart (relleno) será con *
#print(titulo.center(50,"*"))
#suma 10 caracteres más al título
print(titulo.center(len(titulo)+10,'-'))

#alinear titulo a la izquierda
print(titulo.ljust(50,'*'))
#print(titulo.ljust((len(titulo)+10,'_'))

#justificar a la derecha
print(titulo.rjust(50,'*'))

#método replace, reemplazar contenido en un string
#se cubren todos los espacios en blanco eon el caracter que queremos
print(titulo.replace(' ','-'))

#Eliminar caracteres al inicio y final de un str
titulo = ' *** Globalmentoring.com.mx ***'
print(f'Cadena original: {titulo}')
titulo = titulo.strip() #strip quita los espacios en blanco al principio y al final de la cadena
print('Cadena modificada: ')
#r-strip quitamos caracteres a la derecha, lstrip quitamos caracteres a la izquierda
print(f'Cadena modificada: {titulo}'.strip('*').strip())