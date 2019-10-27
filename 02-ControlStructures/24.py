tab = ['Genowefa', 'Onufry', 'Celestyna','Alojzy', 'Pankracy', 'Teofil']
counter = []
for i in tab:
    counter.append(len(i))
max_value = max(counter)
max_value_index = counter.index(max(counter))
print(f'Dlugosc: {max_value} Imię: {tab[max_value_index]}')