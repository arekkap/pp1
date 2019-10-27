parz = 0
np = 0
for i in range(51):
    if i % 2 == 0:
        parz += i
    else:
        np += i
print(f'Suma parzystych ={parz}\nSuma nieparzystych ={np}')