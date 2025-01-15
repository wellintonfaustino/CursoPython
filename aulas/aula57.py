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

salas = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Imprimindo os dados das salas

for sala in salas:
    for numero in sala:
        print(f'Sala: {sala[0]}, Número: {numero}')

# Adicionando um novo aluno