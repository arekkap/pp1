n = int(input('Podaj liczbe: '))
binarny = ''
while n != 0:
    reszta = n % 2
    n = n // 2
    binarny = str(reszta) + binarny
print('Binarny: ', binarny)