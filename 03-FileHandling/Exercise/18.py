tab = []
with open('C:/Users/arekk/Desktop/pp1/03-FileHandling/numbers.txt', 'r') as file:
    for line in file:
        tab.append(int(line))
file.close
print(sorted(tab))