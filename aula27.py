# Fatiamento de strings 
# [incio:fim:passo]
# exemplo: [1:5:2] [incio:fim:passo]

nome = "João"
print(nome[0])  # Imprime 'J'
print(nome[1:3])  # Imprime 'oa'
print(nome[:3])  # Imprime 'Joa'
print(nome[3:])  # Imprime 'ão'

# Fatiamento com passo
print(nome[::2])  # Imprime 'Jão'

# Fatiamento com reversa

print(nome[::-1])  # Imprime 'noaJ'

# Concatenação de strings

nome_completo = nome + " Silva"
print(nome_completo)

# Multiplicação de strings

print(nome * 3)

# Contagem de caracteres

print(len(nome))  # Imprime 4