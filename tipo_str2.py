# help(str.capitalize()
mensaje1 = 'hola mundo'
mensaje2 = mensaje1.capitalize()
print(f'mensaje1: {mensaje1}, id: {hex(id(mensaje1))}') #id nos dice la dirección de memoria
print(f'mensaje2: {mensaje1}, id: {hex(id(mensaje2))}') #hex nos transforma esa dirección a hexadecimal
mensaje1 += 'adios'
print(f'mensaje1: {mensaje1}, id: {hex(id(mensaje1))}') #cambia la posición de memoria

# str.join concatena strings, join pide como entrada un iterable (lista, tupla, diccionario)
help(str.join)

# ejemplo
tupla_str = ('Hola','Mundo','Universidad','Python')
#indicamos que queremos un espacio entre cada uno de los strings
mensaje = ' '.join(tupla_str)
print(f'mensaje: {mensaje}')

lista_cursos = ['Java', 'Python', 'Angular', 'Spring']
#unimos con join los elementos string de la lista
mensaje = ', '.join(lista_cursos)
#imprimimos
print(f'mensaje: {mensaje}')

cadena = 'HolaMundo'
#colocamos puntos enctre cada letra
mensaje = '.'.join(cadena)
print(f'mensaje: {mensaje}')

diccionario = {'nombre':'Juan','apellido':'Perez','edad':'18'}
llaves = '_'.join((diccionario.keys())) #ponemos guion en las keys
valores = '_'.join(diccionario.values()) #ponemos guiones en los valores
print(f'llaves: {llaves}, type: {type(llaves)}')
print(f'valores: {valores}, type: {type(valores)}')


#convertir una cadena a una lista
#pedimos la ayuda, documentación del método
#help(str.split)

cursos = 'Java Python Javascript Angular Spring Excel'
#convertimos string a lista con split
lista_cursos = cursos.split(cursos)
print(f'Lista cursos: {lista_cursos}')

#ahora vamos a crear una cadena pero separados por comas

cursos_separados_comas = 'Java, Python, JavaScript, Angular, Spring, Excel'
lista_cursos = cursos_separados_comas.split(', ') #especificamos separador
print(f'lista cursos: {lista_cursos}')
print(len(lista_cursos)) #podemos ver el número de elementos de la lista

lista_cursos = cursos_separados_comas.split(', ', 3) #max split, máximo de veces que se va a separar la cadena
print(f'lista cursos: {lista_cursos}')
print(len(lista_cursos)) #podemos ver el número de elementos de la lista



