tab = []
with open('C:/Users/arekk/Desktop/pp1/03-FileHandling/numbers.txt', 'r') as file: 
    for line in file:
        if int(line) % 2 == 0:
            tab.append(int(line))
file.close
with open('C:/Users/arekk/Desktop/pp1/03-FileHandling//Exercise/evennumbers.txt', 'a') as file:
    for i in tab:
        file.write(str(i) + '\n')
file.close