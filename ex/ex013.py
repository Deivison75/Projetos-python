#calcula o salario do um funcionario com o almento de 15%

salario = float(input('DIgite o seu salario R$: '))
soma = (15/100) * salario
soma2 = soma + salario

print(f'O seu salario vai sair de {salario} para um almento de 15%, que passa a ser {soma2:.2f}')