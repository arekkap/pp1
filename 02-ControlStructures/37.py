tab = []
for i in range(1,4):
    item = input('Podaj liczbe do mediany: ')
    tab.append(item)
tab.sort()
print(tab[1])