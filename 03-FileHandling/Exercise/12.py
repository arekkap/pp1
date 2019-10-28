produkt=str(input('Podaj produkt: '))
with open('shopping_list.txt','a') as file:
    file.write(produkt)
    file.write('\n')
    file.close