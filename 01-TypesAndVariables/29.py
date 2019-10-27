from random import randint
x = randint(1,6)
y = int(input('Ile zostalo wyrzucone: '))
print(f'Wyrzucono: {x}')
if x == y:
    result = True
else:
    result = False
print(f'Zgadles: {result}')