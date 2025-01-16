# Função com valor padrão

def soma(a, b=10):
    return a + b

print(soma(5))  # Utiliza o valor padrão de b
print(soma(5, 20))  # Utiliza o valor fornecido para b