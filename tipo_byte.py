# Profundizando en el tipo str

#caracteres bytes

caracteres_en_byte = f'Hola Mundo'
print(caracteres_en_byte)

mensaje = b'Universidad Python'
#imprime el valor en bytes de la primera posición, al indicar indice 0
print(mensaje[0])
#con el método chr vemos a que caracter corresponde
print(chr(mensaje[0])) #caracter "U"

#split crea una lista dividiendo las palabras
lista_caracteres = mensaje.split()
print(lista_caracteres)

#convertir de str a bytes
string = 'Programación con Python'
print(f'String original: {string}')

bytes = string.encode('UTF-8')
print('bytes codificados:',bytes)
#convertir bytes a str
string2 = bytes.decode('UTF-8')
print(f'string decodificado: {string2}')
print(string == string2) #comparamos cadenas y da True ya que apuntan al mismo objeto en memoria

