"""
  Listas
"""

# Criar uma lista vazia

lista = []

# Adicionar elementos à lista

lista.append('a')
lista.append('b')
lista.append('c')

# Acessar elementos da lista

print(lista[0])

# Alterar elementos da lista

lista[0] = 'd'

# Remover elementos da lista

del lista[0]

# Contar elementos na lista

print(len(lista))

# Verificar se um elemento está na lista

if 'a' in lista:
  print('Sim, "a" esta na lista.')

# Iterar sobre os elementos da lista

for item in lista:
  print(item)

# Copiar uma lista

nova_lista = lista.copy()

# Ordenar uma lista

lista.sort()

# Buscar um elemento na lista

print(lista.index('c'))

# Adicionar um elemento na lista em uma posição específica

lista.insert(1, 'e')

# Remover um elemento na lista em uma posição específica

lista.pop(1)

# Remover um elemento na lista pelo valor

lista.remove('b')

# Inverter a ordem dos elementos da lista

lista.reverse()

# Unir duas listas

nova_lista += ['d', 'e', 'f']

# Concatenar duas listas

concatenada = lista + nova_lista

# Filtrar elementos de uma lista

filtrada = [item for item in lista if item != 'b']

# Buscar um elemento na lista com busca binária

print(lista.index('b'))