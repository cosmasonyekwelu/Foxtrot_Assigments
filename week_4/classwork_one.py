# ====================== PYTHON FUNCTIONS ASSIGNMENT ======================

# 1. Create a simple function called greet() that returns "Hello World".
# Answer no 1 here.


def greet():
    return "Hello World"


print(greet())


# 2. Create a function called add_numbers() that adds two numbers (5 and 10)
#    inside the function and returns the result.
# Answer no 2 here.


def add_numbers():
    number1 = 5
    number2 = 10
    return number1 + number2


print(add_numbers())

# 3. Create a function called introduction() that returns your name and age in a sentence.
#    Example: "My name is King and I am 25 years old."
# Answer no 3 here.


def introduction():
    name = "Cosmas"
    age = 32
    return f"My name is {name} and I am {age} years old."


print(introduction())

# 4. Create a function called area_of_square() that takes one parameter (side)
#    and returns the area of a square (side * side).
# Answer no 4 here.


def area_of_square(side):
    return side * side


print(area_of_square(6))

# 5. Create a function called multiply_numbers(num1, num2)
#    that returns the product of the two numbers.
#    Call the function three times with different values and print the results.
# Answer no 5 here.


def multiply_numbers(num1, num2):
    return num1 * num2


print(multiply_numbers(9, 5))
print(multiply_numbers(7, 10))
print(multiply_numbers(3, 8))
3

# 6. Create a function that returns True if a number is greater than 10, otherwise returns False.
#    (You can name it check_number)
# Answer no 6 here.


def check_number(num):
    return num > 10


print(check_number(11))
print(check_number(9))

# 7. Demonstrate the difference between a global variable and a local variable
#    inside a function. Use print() to show both.
# Answer no 7 here.


global_var = "I am a global variable"


def variable_local():
    local_var = "I am a local variable"
    return local_var


print(variable_local())

print(global_var)

# 8. Create a function called describe_pet(animal, name)
#    that returns a sentence like "My pet dog is named Rocky."
#    Call it using keyword arguments.
# Answer no 8 here.


def describe_pet(animal, name):
    return f"My pet {animal} is named {name}."


def pet(describe, animal, name):
    return describe(animal, name)


print(pet(describe_pet, "Dog", "Rocky"))

# describe_pet(animal="dog", name="Rocky")


# def msg(name):
#     return f"Hello, {name}!"

# def fun1(fun2, name):
#     return fun2(name)

# # Passing the msg function as an argument
# print(fun1(msg, "Alex"))


# # Passing the msg function as an argument
# print(fun1(msg, "Alex"))


# 9. Create a function called favorite_colors(*colors)
#    that accepts any number of colors and returns them as a tuple.
# Answer no 9 here.


def favorite_colors(*colors):
    return colors


print(favorite_colors("red", "blue", "green"))


# 10. Create a function called student_profile(**data)
#     that accepts any number of keyword arguments (name, age, grade, etc.)
#     and returns them as a dictionary.
# Answer no 10 here.

def student_profile(**data):
    return data


print(student_profile(name="Cosmas", age=32, grade="A", country="Nigeria"))
