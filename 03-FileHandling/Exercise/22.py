with open('C:/Users/arekk/Desktop/pp1/03-FileHandling/Exercise/students.txt', 'r') as file:
    for line in file:
        newline = line.split(',')
        if newline[2] == 'age':
            continue
        if int(newline[2]) < 30:
            print(f'{newline[0]} {newline[1]} {newline[4]}')