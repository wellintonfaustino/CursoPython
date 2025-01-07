#formatação de strings com f-strings

name = "John"
age = 30

print(f"Hello, {name}! You are {age} years old.")

# formatted string literals

print("Hello, {}! You are {} years old.".format(name, age))

# f-string com multiple expressions

print(f"The sum of {age} and 5 is {age + 5}.")

# f-string com dictionary

person = {'name': 'John', 'age': 30}
print(f"Hello, {person['name']}! You are {person['age']} years old.")