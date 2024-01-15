#codigo q verifica se o usuario digitou "santo"

nome = str(input('Digite o nome da cidade em que vc nasceu: ')).strip()
cid = nome[:5].upper()

if cid == 'SANTO':
    print('true')
else:
    print('false')
