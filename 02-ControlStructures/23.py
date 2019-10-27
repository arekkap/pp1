  
ocena = ['celujący', 'bardzo dobry', 'dobry', 'dostateczny',
          'mierny', 'niedostateczny']
ocena.reverse()
mark = int(input('Podaj ocene: '))
print(ocena[mark-1])