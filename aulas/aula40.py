"""
  Calculadora com while
"""
while True:
  sair = input('Quer sair? [s]im: ').lower().startswith('s')
  if sair:
    break
  
  num1 = float(input('Digite o primeiro número: '))
  operador = input('Digite o operador (+, -, *, /): ')
  num2 = float(input('Digite o segundo número: '))
  
  if operador == '+':
    resultado = num1 + num2
    print(f'{num1} + {num2} = {resultado:.2f}')
  elif operador == '-':
    resultado = num1 - num2
    print(f'{num1} - {num2} = {resultado:.2f}')
  elif operador == '*':
    resultado = num1 * num2
    print(f'{num1} * {num2} = {resultado:.2f}')
  elif operador == '/':
    resultado = num1 / num2
    print(f'{num1} / {num2} = {resultado:.2f}')
  else:
    print('Operador inválido.')
  
  print()
