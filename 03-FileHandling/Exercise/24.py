tab = [['Marek', 'Zelnik', 'zelnik@sed.pl'], ['Ewa', 'Maj', 'maje@wp.pl'], ['Piotr', 'Wyga', 'wygap@gop.pl']]
with open('dane.csv', 'w') as file:
    file.write('Imie, Nazwisko, Email\n')
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            string_value = ','.join(tab[j])
            file.write(f'{string_value}\n')
file.close