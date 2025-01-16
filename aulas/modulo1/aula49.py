"""
  For in com listas
"""

lista = ['a', 'b', 'c', 'd', 'e']
contador = 0
for item in lista:
  print(f'{contador + 1}: {item}')
  contador += 1
  print(lista[contador-1])
