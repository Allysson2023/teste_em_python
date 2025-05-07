# https://docs.python.org/3/library/doctest.html

from calculadora import *

# try:
#     print(soma('10', 10))
# except AssertionError as e:
#     print(f'Conta inválida: {e}') 
print()
print()
try:
    print(soma('10', 20, 10))

except AssertionError as errors:
    print(f' - Conta invalida por favor: {errors}')

print()
print()
