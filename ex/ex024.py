#Analisador de Textos

nome = input('Digite seu nome completo: ')
frase = nome.replace(' ', '')

maiusculo = nome.upper()
minuscula = nome.lower()
numero_letra = len(frase)
primeiro_nome = nome.split()

print(maiusculo)
print(minuscula)
print(numero_letra)
print(primeiro_nome[0])