nrDniaTygodnia = 2
counter = 0
print('| PN | WT | SR | CZ | PT | SB | ND |')
print('|',end='')
for x in range(nrDniaTygodnia):
    print('    |',end='')
for i in range(1,8-nrDniaTygodnia):
    print(f' {i}  |', end='')
print('\n')
for a in range(i+1,31):
    counter += 1
    if a >= 10:
        print(f'| {a} ',end='')
    else:
        print(f'|  {a} ',end='')
    if counter % 7 == 0:
        print('|\n')