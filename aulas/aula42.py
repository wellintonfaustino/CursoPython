frase = ('O Python é uma linguem de programação '
         'multiparadigma. Linguagens multiplas '
         'podem ser usadas para resolver muitos problemas.')

# Dividir a frase em palavras
palavras = frase.split()
print(palavras)

# Contar quantidade de palavras
print(f"Quantidade de palavras: {len(palavras)}")

# Contar a letra que mais se repete
letras = {}
for char in frase:
    if char.isalpha():  # Verificar se o caractere é uma letra
        char = char.lower()  # Converter para minúsculo para evitar duplicidade
        letras[char] = letras.get(char, 0) + 1  # Incrementar o contador da letra

# Encontrar a letra mais frequente
mais_frequente = max(letras, key=letras.get)  # Letra com maior frequência
frequencia = letras[mais_frequente]

print(f'A letra que mais se repete na frase é "{mais_frequente}", aparecendo {frequencia}x.')
