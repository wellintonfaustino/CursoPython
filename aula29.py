"""
Introdução ao try/except

# O try/except é utilizado para lidar com erros que podem ocorrer durante a execução de um código.
"""

try:
    # Tentativa de execução de código
    print(10/0)
except ZeroDivisionError:
    # Caso ocorra um ZeroDivisionError, será executado este bloco
    print("Divisão por zero.")

# O try/except também pode ser utilizado para lidar com outros tipos de erros que podem ocorrer durante a execução de um código.