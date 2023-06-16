#profundizando str

#multiplicación str
resultado = 50*' Hola'
print(f'Resultado: {resultado}')

#multiplicación de tuplas
resultado = 5* ('Hola','Perro',)
print(f'Resultado: {resultado}')

#multiplicando listas
resultado = 10*[0]
print(f'Resultado: {resultado}, largo: {len(resultado)}')

#caracteres de escape
resultado = 'Hola \' Mundo'
print(f'Resultado: {resultado}')

#backspace
resultado = 'Se va a eliminar el punto.\b'
print(f'Resultado: {resultado}')

#doble backspace
resultado = 'Se va a eliminar los últimos dos caracteres.\b\b'
print(f'Resultado: {resultado}')

# Caracter \ con la \\ evitanmos por ejemplo el \n-uevo
resultado = 'c:\\directorio\\juan'
#backspace
print(f'Resultado: {resultado}')

#raw string, poner r para que no se haga salto de línea
resultado = r'Cadena con \n salto de línea'
print(f'Resultado: {resultado}')

#caracteres unicode (todos los caracteres en python usan esa representación)
# con \u podemos poner el código unicode
print('Hola\u0020Mundo')
#se imprime la A mayúscula
print('Notación simple:', '\u0041')
#8 caracteres
print('Notación extendida: ','\U00000041')
#hexadecimal
print('Notación hexadecimal','\x41')
print('Corazón','\u2665')
print('Cara sonriendo: ','\U0001f600')
#U000 = U+
print('Corazón','\U0001f40d')


#ASCII
#pasamos el valor en decimal
caracter = chr(65)
print('A mayúscula', caracter)
caracter = chr(64)
print('A mayúscula', caracter)
caracter = chr(97)
print('A mayúscula', caracter)




