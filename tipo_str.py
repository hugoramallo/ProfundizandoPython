# Profundizando en el tipo str (string)
# STR es una clase ya incluída (built-in) en Python
import math

import mi_clase

# Concatenación automática en python
# Podemos concatenar con + o también sin signo
variable = 'Adios'
mensaje = 'Hola' + 'Mundo'
print(mensaje)
mensaje = 'Hola' 'Mundo' +  variable
mensaje += 'Universidad' 'Python'
print(mensaje)

#función help, se importa por default, tiene métodos downer
#analizamos capitalize, si ponemos paréntesis llamamos a la función, sino no
help(str.capitalize)
# Ponemos con la primera letra en mayúsculas una palabra
help(str.capitalize('hola'))
# Pedimos información sobre Math.isnan
help(math.isnan)
help(math)
help(str)

# Pedimos info de la documentación de nuestra clase
#help(mi_clase)

#también se puede hacer con el método print y __doc__

print(mi_clase.MiClase.__doc__)
print(mi_clase.MiClase.__init__.__doc__)
print(mi_clase.MiClase.mi_metodo.__doc__)
print(mi_clase.MiClase.mi_metodo)
print(type(mi_clase.MiClase.mi_metodo))
