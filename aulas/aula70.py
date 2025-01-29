# Retorno de função

def return_function(x: any):
  return lambda y: x + y

# Uso do retorno de função

double = return_function(2)
print(double(5))  # Saída: 10