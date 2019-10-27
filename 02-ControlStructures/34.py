pesel = input('Podaj pesel: ')
wiek = 2019 - int(pesel[:2]) - 1900
print(f'Wiek: {wiek}')
if int(pesel[9]) % 2 == 0:
    print('Plec: Kobieta')
else:
    print('Plec: Mezczyzna')