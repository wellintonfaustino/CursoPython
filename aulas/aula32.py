numero = input("Informe um número Inteiro:\n")

# Valida se número é um número
if not isinstance(numero, int):
  print("Informe um número inteiro")
  exit()

numero = numero % 2

if numero == 0:
  print("Par")
else:
  print("Impar")