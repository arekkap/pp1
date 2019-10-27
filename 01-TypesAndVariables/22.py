a=float(input('Podaj bok A: '))
b=float(input('Podaj bok B: '))
c=float(input('Podaj bok C: '))
import math
s=math.sqrt((a+b+c)*(a+b-c)*(a-b+c)*(-a+b+c))/4
print(f'Pole trojkata wynosi: {s}')