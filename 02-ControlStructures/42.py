x = int(input('Podaj dzielna: '))
y = int(input('Podaj dzielnik: '))
if y == 0:
    print('Dzielenie przez 0!')
while y != 0:
    print(x/y)
    break