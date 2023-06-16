# Manejo de valores infinitos
import math
from decimal import Decimal

infinito_positivo = float('inf')
print(f'a: {infinito_positivo}')
# preguntamos si el valor es infinito
print(f'Es infinito: {math.isinf(infinito_positivo)}')

infinito_negativo = float('-inf')
print(f'a: {infinito_negativo}')
print(f'Es infinito: {math.isinf(infinito_negativo)}')

# Módulo Math
infinito_positivo = math.inf
print(f'a: {infinito_positivo}')
print(f'Es infinito: {math.isinf(infinito_positivo)}')

infinito_negativo = -math.inf
print(f'a: {infinito_negativo}')
print(f'Es infinito: {math.isinf(infinito_negativo)}')

# Módulo Décimal
infinito_positivo = Decimal('Infinity')
print(f'a: {infinito_positivo}')
print(f'Es infinito: {math.isinf(infinito_positivo)}')

infinito_negativo = Decimal('-Infinity')
print(f'a: {infinito_negativo}')
print(f'Es infinito: {math.isinf(infinito_negativo)}')

