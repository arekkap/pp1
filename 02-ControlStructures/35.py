from math import sqrt
a = float(input('Podaj a: '))
b = float(input('Podaj b: '))
c = float(input('Podaj c: '))
delta = b**2 - 4*a*c
if delta <0:
    print('Brak mniejsc zerowych')
x1 = (-b + sqrt(delta))/(2*a)
x2 = (-b - sqrt(delta))/(2*a)
print(f'Miejsca zerowe: {x1} i {x2}')