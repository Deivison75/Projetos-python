#conversor de medida

metros = float(input('Digite a distancia em metros: '))
km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros * 10
cm = metros * 100
mm = metros * 1000

print('A distancia convertida de {} é:'.format(metros))
print(f'{km}Km')
print(f'{hm}hm')
print(f'{dm}dam')
print(f'{dm:.0f}dm')
print(f'{cm:.0f}cm')
print(f'{mm:.0f}mm')