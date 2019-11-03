import re
suma = 0
with open('C:/Users/arekk/Desktop/pp1/03-FileHandling/land.txt', 'r') as file:
     file = file.read()
     numbers = re.findall('[0-9]',file)
     for i in numbers:
         suma += int(i)
     print(f'Suma cyfr: {suma}')