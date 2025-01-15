"""
  Tupla dentro de lista
"""

dados = [
    ('João', 25, 'M'),
    ('Maria', 30, 'F'),
    ('Pedro', 28, 'M')
]

# Imprimindo os dados
for nome, idade, sexo in dados:
    print(f'Nome: {nome}, Idade: {idade}, Sexo: {sexo}')