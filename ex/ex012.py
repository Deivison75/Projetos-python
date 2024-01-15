#calcula a porcentagem e dar um desconto em um produto

p = float(input('Digite o preço do produto R$: '))
d = float(input('Digite o desconto que sera aplicado: '))
soma = (d/100) * p
desconto = p - soma

print(f'O valor do produto com o desconto aplicado é:{desconto:.2f}')