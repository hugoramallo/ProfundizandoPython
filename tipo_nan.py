import math
from decimal import Decimal
# Tipo Nan (Non a Number)
# Resultado de operación matemática similar a valores infinitos
# NaN no es sensible a mayúsculas/minúsculas
# Tipo de dato numérico para representar un valor indefinido
a = float('NaN')
print(f'a: {a}')
print(f'Es NaN (not a number)?: {math.isnan(a)}')

a = Decimal('NaN')
print(f'a: {a}')
print(f'Es NaN (not a number)?: {math.isnan(a)}')