#codigo que calcula a tamgente cosseno e seno

from math import cos, sin, radians, tan

an = float(input('digite o ângulo: '))

co = cos(radians(an))#calcula o cosseno
print(f'O cosseno é: {co:.2f}')

si = sin(radians(an))#calcula o seno
print(f'O seno é: {si:.2f}')

ta = tan(radians(an))#calcula a tamgente
print(f'A tangente é: {ta:.2f}')
