limit = int(input('Podaj limit predkosci: '))
pred = int(input('Podaj predkosc pojazdu: '))
roznica = pred - limit
counter = -10
if roznica <= 0:
    print('Bez mandatu')
elif roznica > 0 and roznica <= 10:
    print(f'Mandat: {roznica*5}')
elif roznica > 10:
    for i in range(roznica):
        counter += 1
    print(f'Mandat: {50+counter*15}')