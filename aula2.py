# print com números e conta
print(2-4)

# print com texto
print('Print com Texto')

# print com variável
nome = 'Joaquim'
print(f'Print com variável {nome}')

# print com separador, utilizando 'sep' para separador
print(1, 2, 3, sep=' - ')


# print com end, utilizando 'end' para quebra de linha
print('Print com end', end=' - ')
print('Print com end')

# print com formatação, utilizando 'format' para formatação
print('Print com formatação {0} - {1}'.format(10, 20))
print('Print com formatação {a} - {b}'.format(a=10, b=20))

# print com expressão lambda
print('Print com expressão lambda', (lambda x: x*2)(5))