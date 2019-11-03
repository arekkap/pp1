tab = []
numbers = 0
suma = 0 
with open('C:/Users/arekk/Desktop/pp1/03-FileHandling/numbersinrows.txt','r') as file:
    for line in file:
        newline = line.split(',')
        numbers += len(newline)
        for i in newline:
            suma += int(i)
file.close
print(f'Ilosc liczb: {numbers}\nSuma liczb: {suma}')