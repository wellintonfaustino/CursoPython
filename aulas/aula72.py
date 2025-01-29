# Exercicio

# Crie uma função que multiplçica todos argumentos não nomeados recebidos
# Retorne o toral para a variavel e mostre o valor

def multiply_args(*args):
    total = 1
    for arg in args:
        total *= arg
    return total

# Teste a função

result = multiply_args(2, 3, 4, 5)
result

print(result)

# Crie uma função que fale se um número é par ou impar

def is_even(number):
    return number % 2 == 0

# Teste a função

print(is_even(4))
print(is_even(5))