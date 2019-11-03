tab = []
with open('C:/Users/arekk/Desktop/pp1/03-FileHandling/universities.txt', 'r') as file:
    for line in file:
        tab.append(line)
file.close
with open('C:/Users/arekk/Desktop/pp1/03-FileHandling/universities.txt', 'w') as file:
    for i in sorted(tab):
        file.write(i)
file.close