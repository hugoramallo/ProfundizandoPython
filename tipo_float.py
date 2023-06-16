# Tipo float
a = 3.0
print(f'a: {a}')
# Dos decimales
print(f'a: {a:.2f}')
# Constructor float puede recibir tanto int como str
a = float(10)
# sobrecargamos el constructor (pasamos varios tipos de datos al mismo constructor)
a = float('10')
print(f'a: {a:.2f}')
# Notación exponencial (valores positivos o negativos)
a = 3e5
print(f'a: {a:.2f}')
a = 3e-5
print(f'a: {a:.5f}')
# Cualquier cálculo que involucre un float, todo se promueve a float
a = 4.0 + 5
print(f'a: {a:.2f}')
print(type(a))
