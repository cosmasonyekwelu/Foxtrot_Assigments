# ====================== PYTHON LOOPS ASSIGNMENT ======================

# 1. Use a while loop to print the numbers from 1 to 15.
# Answer no 1 here.
num = 1
while num <= 15:
    print(num)
    num += 1

# 2. Use a while loop to print only the even numbers between 1 and 20.
# Answer no 2 here.
num = 2
while num <= 20:
    print(num)
    num += 2

# 3. Given a list of names = ["Anna", "Bola", "Chris", "Dayo"],
#    use a for loop to print each name in the list.
# Answer no 3 here.
names = ["Anna", "Bola", "Chris", "Dayo"]
for name in names:
    print(name)

# 4. From the list numbers = [2, 4, 6, 8, 10],
#    use a for loop to multiply each number by 3
#    and add the results into a new list. Print the new list.
# Answer no 4 here.
numbers = [2, 4, 6, 8, 10]
new_list = []
for num in numbers:
    new_list.append(num * 3)
print(new_list)

# 5. Use a for loop to check if "Chris" is in the list of names = ["Anna", "Bola", "Chris", "Dayo"].
#    If found, print "Chris found" and break the loop.
# Answer no 5 here.
names = ["Anna", "Bola", "Chris", "Dayo"]
for name in names:
    if name == "Chris":
        print("Chris found")
        break

# 6. Given list fruits = ["apple", "banana", "orange"],
#    use a for loop to add "@fruit.com" to each fruit and store them in a new list.
#    Print the new list.
# Answer no 6 here.
fruits = ["apple", "banana", "orange"]
email_list = []
for fruit in fruits:
    email_list.append(fruit + "@fruit.com")
print(email_list)

# 7. Use a while loop to keep adding 5 to a number until it becomes greater than 50.
#    Print the number at each step.
# Answer no 7 here.


# 8. Write a for loop that checks through numbers = [1,2,3,4,5,6].
#    If it finds the number 4, print "Found 4" and stop the loop.
#    If it doesn’t find 4, print "4 not found".
# Answer no 8 here.


# 9. Given two lists:
#    list1 = [1, 2, 3]
#    list2 = [4, 5, 6]
#    Use a for loop to add all the numbers in list2 into list1.
#    Print the final list1.
# Answer no 9 here.


# 10. Given names = ["John", "Mary", "Paul"],
#     write a loop to remove "Mary" from the list if it exists.
#     Print the updated list.
# Answer no 10 here.
