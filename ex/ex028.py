nome = str(input('Digite um qualquer coisa: ')).upper().strip()
print('Oq você digitou tem {} letras a'.format(nome.count('A')))
print('A letra A foi vista pela primeira vez na posição {}'.format(nome.find('A')+1))
print('A letra A foi vista por ultimo na posição {}'.format(nome.rfind('A')+1))

