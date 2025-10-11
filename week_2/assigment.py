# ====================== PYTHON DATA STRUCTURES ASSIGNMENT ======================

# ----------- DICTIONARY -----------

# 1. Create a dictionary called car with keys: "brand", "model", "year".
#    Give them values and print the dictionary.
# Answer no 1 here.

car = {"brand": "Benz", "model": "C 300", "year": 2012}
print("Car dictionary:", car)

# 2. From a dictionary called book = {"title": "Python 101", "author": "James", "year": 2022},
#    print only the title and author.
# Answer no 2 here.
book = {"title": "Python 101", "author": "James", "year": 2022}
print(book["title"], book["author"])


# 3. Change the value of "year" in book to 2024 and print the dictionary.
# Answer no 3 here.
book["year"] = 2024
print(book)


# 4. Add a new key "pages" with any number value to the dictionary book.
# Answer no 4 here.
book["pages"] = 100
print(book)


# 5. Delete the "author" key from the dictionary book and print it.
# Answer no 5 here.
del book["author"]
print(book)

# ----------- LIST -----------

# 6. Create a list of 5 countries and print the first and last country.
# Answer no 6 here.
countries = ["Nigeria", "Ghana", "Niger", "Kenya", "South Africa"]
print("First country:", countries[0], "and Last country:", countries[4])


# 7. Replace the 2nd item in your list of countries with "Canada".
# Answer no 7 here.
countries[1] = "Canada"
print(countries)

# 8. Delete the 3rd item in your list of countries.
# Answer no 8 here.
del countries[2]
print(countries)


# 9. Concatenate [10, 20, 30] with [40, 50, 60] and print the new list.
# Answer no 9 here.
list1 = [10, 20, 30]
list2 = [40, 50, 60]
new_list = list1 + list2
print("Concatenated list:", new_list)


# 10. Check if "Kenya" exists inside your list of countries and print the result.
# Answer no 10 here.
kenya_exists = "Kenya" in countries
print("Is Kenya in countries list?", kenya_exists)


# 11. Create a list with the word "Hello" repeated 4 times.
# Answer no 11 here.
hello_list = ["Hello"] * 4
print(hello_list)


# 12. Use append() to add "Japan" to your list of countries.
# Answer no 12 here.
countries.append("Japan")
print(countries)

# 13. Use insert() to add "Brazil" at position 2 in your list of countries.
# Answer no 13 here.
countries.insert(2, "Brazil")
print(countries)


# 14. Use pop() to remove the last item from a list of numbers = [100, 200, 300, 400].
# Answer no 14 here.
numbers = [100, 200, 300, 400]
popped_item = numbers.pop()
# print("After removing the last number:", numbers)


# 15. Use remove() to delete the number 200 from the list numbers = [100, 200, 300, 400].
# Answer no 15 here.
numbers = [100, 200, 300, 400]
numbers.remove(200)
# print("After removing the number 200:", numbers)


# ----------- NESTED LIST -----------

# 16. Given nested = [1, [2, 3, {"letters": ["a", "b", "c"]}], 4]
#     - Print the value "b"
#     - Add "d" into the "letters" list
# Answer no 16 here.
nested = [1, [2, 3, {"letters": ["a", "b", "c"]}], 4]
print(nested[1][2]["letters"][1])
nested[1][2]["letters"].append("d")


# ----------- TUPLE -----------

# 17. Create a tuple of 4 animals and print the second animal.
# Answer no 17 here.
animals = ("Goat", "Cow", "Fish", "Snake")
print(animals[1])


# 18. Try to change one value in the tuple. What happens? (Write the answer in a comment)
# Answer no 18 here.

# animals[0] = "Chicken" Error in console: TypeError: 'tuple' object does not support item assignment

# 19. Count how many times "cat" appears in the tuple: pets = ("cat", "dog", "cat", "bird").
# Answer no 19 here.
pets = ("cat", "dog", "cat", "bird")
cat_count = pets.count("cat")
# print(cat_count)


# ----------- SET -----------

# 20. Create two sets:
#     set1 = {"apple", "banana", "cherry"}
#     set2 = {"banana", "mango", "cherry"}
#     - Find the intersection
#     - Find the union
#     - Find the difference (set1 - set2)
# Answer no 20 here.
set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "mango", "cherry"}
intersection = set1.intersection(set2)
union = set1.union(set2)
difference = set1.difference(set2)
# print("Intersection:", intersection)
# print("Union:", union)
# print("Difference:", difference)
