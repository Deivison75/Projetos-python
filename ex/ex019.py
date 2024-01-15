#Codigo q calcula a ipotenusa e o cateto
import math

cateto1 = float(input('Digite o cateto oposto: ')) 
cateto2 = float(input('digite a cateto adjacente: '))
soma = math.sqrt(cateto1**2 + cateto2**2)

print(f'A medida da Hipotenusa é:{soma:.2f}')