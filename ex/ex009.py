#Tabuada

num = int(input('Digite a tabuada que voce deseja ver: '))

for i in range(1, 11):
    resultado = num * i
    print(f'{num} x {i} = {resultado}')