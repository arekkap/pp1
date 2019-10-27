tab = []
x = int(input('Podaj pierwsza liczbe: '))
tab.append(x)
y = int(input('Podaj druga liczbe: '))
tab.append(y)
z = int(input('Podaj trzecia liczbe: '))
tab.append(z)
tab.sort()
print(' '.join(map(str,tab)))