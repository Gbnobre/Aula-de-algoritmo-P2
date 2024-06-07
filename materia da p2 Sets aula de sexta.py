# Sets(conjuntos) (São elementos unicos que não se repetem)

planeta_anao = {'Ceres', 'Plutão', 'Eris', 'Haumea', 'Makemake'}

print('\033[37;1m')
print(planeta_anao)

# Buscando a quantidade de valores dentro do Set com LEN
print('\nA quantidade de planetas são ', len(planeta_anao))
print('\033[34m')

# Percorre o Set com o *for* e printa todos os valores com letra maiuscula com metodo .upper
for planeta in planeta_anao:
    print(planeta.upper())
    
print('\033[35m')
for planeta in planeta_anao:

    print(planeta.lower())

print('\033[30;1m')

# Condição para buscar um valor dentro do Set
if 'Plutão' in planeta_anao:
    print('Este planeta anão que é Plutão existe dentro do conjunto')
else:
    print('Este planeta não existe no conjunto')

# Confimando um valor dentro do Set 
print('')
print('Plutão' in planeta_anao)

print('\033[36m')
astros = ['Terra', 'Plutão', 'Marte', 'Marte', 'Marte', 'Marte', 'Terra', 'Venus', 'Lua', 'Jupiter']
astrosSet = set(astros)
print('Nova lista >', astros)
print('\033[34m')
print('Virou um Set >', astrosSet)

print('\033[32m')
astrosList = list(astrosSet)
print('Virou lista de novo >', astrosList)

print('\033[37m')
planetas1 = {'Terra', 'Marte', 'Urano', 'Neturno'}
planetas2 = {'Terra', 'Jupiter', 'Urano', 'Saturno', 'Venus'}
print('A intercessão que tem entre os 2 são', planetas1&planetas2)
# Outra forma de fazer e com o metodo .intersection e o operador é o &

print('')
print(planetas1 - planetas2) 
print(planetas2 - planetas1)  
# Outra forma de fazer e com o metodo .difference e o operador é o -

print('')
print(planetas1 ^ planetas2)
# Outra forma de fazer e com o metodo .symetric_difference e o operador é o ^

print('')
planetas3 = {'Jupiter', 'Saturno'}
print(planetas1.isdisjoint(planetas2))
print(planetas1.isdisjoint(planetas3))

# Para adicionar um valor no Set
print('\033[33m')
planetas3.add('Terra')
print(planetas3)

# Para remover um valor do Set
print('\033[31m')
planetas3.remove('Terra')
print(planetas3)

# Remove tambem mas nao tendo o valor ele nao da erro como *remove* 
print('\033[36m')
planetas3.discard('Lua')
print(planetas3)

print('')
planetas3.clear()
print(planetas3)
 
print('')
planetas4 = {'Terra', 'Marte', 'Urano', 'Neturno'}
print('O planeta que saiu foi:', planetas4.pop())  
print('\033[37;1m')

# PARA FAZER A UNIAO DOS SETS USE O OPERADOR | OU OM METODO .UNION


