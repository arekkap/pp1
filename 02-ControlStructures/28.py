a = int(input('Bok A: '))
b = int(input('Bok B: '))
for i in range(1, a+1):
    if i == 1:
        print('*'*b)
    if i >= 2 and i < b:
        print('*' + ' '*(b-2) + '*')
    if i == b:
        print('*'*b)