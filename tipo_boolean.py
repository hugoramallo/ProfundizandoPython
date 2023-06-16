#bool contiene los valores de True y False
# Tipos numéricos, False para el valor de 0, True para los demás valores
valor = 0
resultado = bool(valor)
print(f'Valor {valor:.2f}, resultado: {resultado}')
valor = 15
resultado = bool(valor)
#print(f'Valor {valor}, resultado: {resultado}')
# Tipo str (string), False para '', True, todo lo que no sea 0 es verdadero
valor = 'Hola'
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')

# Tipo colecciones, False pra colecciones vacias, True para todas las demás.
# Lista
valor = [2,3,'4']
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')

# Tupla
valor = (2,3,4)
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')

#Diccionario
valor = {"Nombre":"Juan","2":"8","3":"7"}
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')

# Bool comprueba si la cadena vacia es falsa o verdadera
# Si la cadena está llena, devuelve verdadero

if bool(''):
    print('Regresó verdadero')
else:
    print ('Regresó falso')

if bool('33a3'):
    print('Regresó verdadero')
else:
    print ('Regresó falso')
# Sin bool haría lo mismo, si está vacía es falso y llena verdadera
if '':
    print('Regresó verdadero')
else:
    print ('Regresó falso')

# Lo mismo con una variable
variable = '444'
if variable:
    print('Regresó verdadero')
else:
    print ('Regresó falso')
# con 0 devuelve siempre falso, con cualquier otra cosa verdadero
variable = 0
if variable:
    print('Regresó verdadero')
else:
    print ('Regresó falso')

# Ciclo/Bucle While
# Se ejecutaría de manera infinita mientras sea cierta 'No esté vacía'
variable = [1,2]
while variable:
    print('ejecución ciclo while')
    # Con break, únicamente se ejecuta una vez
    break
else:
    print('fin ciclo while')