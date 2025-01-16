"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
   7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf = "49423329829"

cpf = cpf.replace(".", "").replace("-", "")

print(f'CPf: {cpf}')
contagem = 10
soma = 0

# Remove os ultimos 2 dígitos

cpf = cpf[:-2]

print(f'CPF sem os ultimos dois digitos: {cpf}')


for digito in cpf:
    soma += int(digito) * contagem
    contagem -= 1

resto = soma % 11

if resto < 2:
    primeiro_digito = 0
else:
    primeiro_digito = 11 - resto

print(primeiro_digito)

"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0

"""

cpf = "49423329829"

cpf = cpf.replace(".", "").replace("-", "")

print(f'CPf: {cpf}')

contagem = 11

soma = 0

# Remove os ultimo dígito

cpf = cpf[:-1]

print(f'CPF sem o ultimo digito: {cpf}')

for digito in cpf:
    soma += int(digito) * contagem
    contagem -= 1

resto = soma % 11

if resto < 2:
    segundo_digito = 0
else:
    segundo_digito = 11 - resto

print(segundo_digito)

# Gerador de cpf

def gera_cpf():
    import random

    cpf = ""
    for _ in range(9):
        cpf += str(random.randint(0, 9))

    contagem = 10
    soma = 0

    print(f'Cpf: {cpf}')

    for digito in cpf:
        soma += int(digito) * contagem
        contagem -= 1

    resto = soma % 11

    if resto < 2:
        primeiro_digito = 0
    else:
        primeiro_digito = 11 - resto
    
    cpf += str(primeiro_digito)
    
    contagem = 11
    soma = 0
    for digito in cpf:
        soma += int(digito) * contagem
        contagem -= 1

    resto = soma % 11
    if resto < 2:
      segundo_digito = 0
    else:
        segundo_digito = 11 - resto

    cpf += str(segundo_digito)
    return cpf

print(gera_cpf())