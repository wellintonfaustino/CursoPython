"""
  Iteradores
"""
texto = iter('Wellinton')

# next
for _ in range(len(texto)):
  print(next(texto))

# iter

iterador = iter(texto)
while True:
  try:
    print(next(iterador))
  except StopIteration:
    break

"""
  Geradores
"""

def gerador():
  yield 'a'
  yield 'b'
  yield 'c'

ger = gerador()
print(ger)
