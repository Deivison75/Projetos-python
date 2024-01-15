#programa q verifica se o nome do usuario contem 'silva'
nome = input('Qual e seu nome conpleto? ').strip()

if 'SILVA' in nome.upper():
    print('O seu nome contem Silva!')
else:
    print('O seu nome não contem Silva')