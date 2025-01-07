"""
Exercicio
Informar o nome do usuário
Informar idade

Se o nome do usuário e idade forem digitados:
  Exiba:
    O seu nome é {nome}
    Você tem {idade} anos
    Nome invertido
    Se o nome contem ou não espaços
    Quantidade de letras do nome
    Listar a primeira e ultima letra do nome
"""

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade.isdigit():
  nome = nome.strip()
  idade = int(idade)
  
  print(f'O seu nome é {nome}')
  print(f'Você tem {idade} anos')
  print(f'Nome invertido: {nome[::-1]}')
  print(f'Seu nome tem ou não espaços: {"tem espaço" if " " in nome else "não tem espaço"}')
  print(f'Quantidade de letras do nome: {len(nome)}')
  print(f'Primeira letra do nome: {nome[0]}')
  print(f'Ultima letra do nome: {nome[-1]}')
else:
  print('Nome e idade devem ser digitados.')