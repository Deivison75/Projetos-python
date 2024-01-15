#mostra os tipos q qualquer coisa digitada 
a = input('Digite algo: ')

print('O tipo é: ', type(a))
print('Ele é um numero? ', a.isnumeric())
print('Ele é afalbetico? ', a.isalpha())
print('Ele possue espaço? ', a.isspace())
print('ELe esta em letras maiusculas:', a.isupper())
print('Ele esta em letras minusculas', a.islower())
