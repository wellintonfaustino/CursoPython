# f-strings

name = "John"
age = 30

print(f"Hello, {name}! You are {age} years old.")

# formatted string literals

print("Hello, {}! You are {} years old.".format(name, age))

# f-string with multiple expressions  

print(f"The sum of {age} and 5 is {age + 5}.")

# f-string with dictionary

person = {"name": "John", "age": 30}
print(f"Hello, {person['name']}! You are {person['age']} years old.")

# formatar número com 2 casas decimais

imc =  18.52569
print(f"The IMC is {imc:.2f}.")
print("The price is {:.2f}.".format(99.99999))