#codigo q excolhe o nome de um aluno
import random

n1 = str(input('Nome do primeiro aluno: '))
n2 = str(input('Nome do seundo aluno: '))
n3 = str(input('Nome do segundo aluno: '))
n4 = str(input('Nome do quarto aluno: '))
lista = [n1, n2, n3, n4]

sorteado = random.choice(lista)
print(f'O aluno sorteado é {sorteado}')
