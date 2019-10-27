nazwy = ['zero', 'jeden', 'dwa', 'trzy', 'cztery', 'pięć', 'sześć', 'siedem', 'osiem', 'dziewięć']
liczba = input('Podaj liczbe: ')
print(liczba, end = ' - ')
for i in liczba:
    print(nazwy[int(i)], end = ' ')   