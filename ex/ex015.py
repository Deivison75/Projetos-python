#calcular o aluguel do carro

dias = int(input('Quantos dias você ficou com o carro? '))
km = float(input('Quantos km vc percorrel com o veiculo? '))
soma_dias = dias * 60
soma_km = 0.15 * km
soma_total = soma_dias + soma_km

print(f'Você tera que pagar R${soma_total:.2f}! Pelo aluguel do carro.')
