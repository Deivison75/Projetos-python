#calcula os metros quadrados de uma parede e calcula a quantidade de tinta gasta

largura = float(input('Coloque a largura: '))
altura = float(input('Coleque a altura: '))
mq = altura * largura
tinta = mq / 2

print(f'A parede tem {mq}m² e você vai gastar {tinta}L de tinta')
