# ====================== PYTHON BEGINNER ASSIGNMENT ======================

# 1. Write:
#    - One single-line comment about Python (use #)
#    - One multi-line comment about Python (use ''' ''' or """ """)


# Python is a powerful programming language used for web, data science, machine learning, and automation.

"""
Python is known for its simplicity and readability, making it an excellent choice for beginners.
It has a vast ecosystem of libraries and frameworks that support various applications,
from web development to artificial intelligence.
"""

# 2. Make 5 variables with these types:
#    - A string (text)
#    - An integer (whole number)
#    - A float (number with decimal)
#    - A boolean (True or False)
#    - Another string using snake_case (example: my_name)


cohort = "foxtrot"
student_count = 5
average_score = 90.5
is_enrolled = True
favorite_color = "green"


# 3. Use x = 10 and y = 3
#    Print the answer AND the type for:
#    - x + y
#    - x - y
#    - x * y
#    - x / y
#    - x // y


x = 10
y = 3

print("x + y:", x + y, "Type:", type(x + y))
print("x - y:", x - y, "Type:", type(x - y))
print("x * y:", x * y, "Type:", type(x * y))
print("x / y:", x / y, "Type:", type(x / y))
print("x // y:", x // y, "Type:", type(x // y))


# 4. Join (concatenate) two strings to make a sentence, then print it.

greeting = "Hello"
name = "Cosmas"
message = greeting + " " + name
print(message)

# 5. Print the word "Python" three times using * (multiplication).

print("Python" * 3)


# 6. Change (cast) these and print the value and type:
#    - 45.89 ➝ integer
#    - 78 ➝ string
#    - "1234" ➝ float

float_to_int = int(45.89)
print("45.89 as integer:", float_to_int, "Type:", type(float_to_int))

int_to_string = str(78)
print("78 as string:", int_to_string, "Type:", type(int_to_string))

string_to_float = float("1234")
print('"1234" as float:', string_to_float, "Type:", type(string_to_float))


# 7. Make a variable called country.
#    Change it 3 times to different countries.
#    Print the final one.

country = "Nigeria"
country = "Canada"
country = "France"
print(country)


# 8. Make a sentence using + to join strings.
#    Example: "My name is " + your_name + " and I like " + your_hobby

course = "Backend with Python Django"
duration = "12 weeks"
institution = "Univelcity"

sentence = "I am studying " + course + " for " + \
    duration + " at " + institution + "."
print(sentence)


# 9. What will this show?
#    result = "5" + "7"
#    print(result, type(result))
#    Write your answer here as a comment:

# This will show: "57" <class 'str'>
# When using + with strings, it performs concatenation, not mathematical addition.
# So "5" + "7" joins the two strings together to form "57", and the type remains string.


# 10. Create two variables with numbers.
#     Add them together, but before printing, convert the result to a string.
#     Then print it inside a sentence like: "The answer is 10"

apples = 6
oranges = 4
total = apples + oranges
result_string = str(total)
print("The answer is " + result_string)
