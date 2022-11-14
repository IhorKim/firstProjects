# Task
"""
Assign values to variables
"""
s = "10 5 -6"
x, y, z = s.strip().split()  # x, y, z strings here
print(f"{x = }, {y = }, {z = }")
print("-" * 80)


# Task
"""
Convert x, y, z into integers. Python's map() is a built-in function that allows you
to process and transform all the items in an iterable without using an explicit for loop, a technique commonly
known as mapping. map() is useful when you need to apply a transformation function to each item in an iterable
and transform them into a new iterable.
"""
s = "10 5 6"
x, y, z = s.strip().split()  # x, y, z strings here
x, y, z = map(int, (x, y, z))  # x, y, z integers here
volume = x * y * z
print(f"{volume}")
print("-" * 80)


# Task
"""
Using reduce function. Python's reduce() is a function that implements a mathematical technique called 
folding or reduction. reduce() is useful when you need to apply a function to an iterable and reduce it 
to a single cumulative value.
"""
from functools import reduce
s = "10 5 7"
volume = reduce(
    lambda x, y: x * y,
    map(int, s.strip().split())
)
print(f"{volume}")
print("-" * 80)


# Task
"""
List comprehension in Python is a concise way of creating lists from the ones that already exist. It provides 
a shorter syntax to create new lists from existing lists and their values
"""
names = ["Alexander", "Viktoriia", "Aiden", "Aaron", "Ihor"]
names_starts_a = []
for name in names:
    if name.startswith("A"):  # looking for names starts with "A"
        names_starts_a.append(name)
print(names_starts_a)

names2 = [i for i in names if i.startswith("A")]  # List comprehension
print(names2)
print("-" * 80)


# Task
"""
Filter() is a built-in function in Python. The filter function can be applied to an iterable such as a list 
or a dictionary and create a new iterator. This new iterator can filter out certain specific elements based 
on the condition that you provide very efficiently
Filter returns iterator. We need to convert iterator into list for example, or tuple
"""
names = ["Alexander", "Viktoriia", "Aiden", "Aaron", "Ihor"]
names_starts_a = filter(lambda x: x.startswith("A"), names)
print(list(names_starts_a))
print("-" * 80)


# Task
"""
Making copy a list
"""
numbers = [1, 2, 3]
numbers2 = numbers[:]
numbers2.append(56)
print(numbers)
print(numbers2)
print("-" * 80)


# Task
"""
Reverse a list
"""
numbers = [1, 2, 3]
numbers2 = numbers[::-1]
print(numbers2)
print("-" * 80)


# Task
"""
Using tuple
"""
name = "Ihor"
# if name == "Alexander" or name == "Iryna" or name == "Ihor" or name == "Viktoriia" or name == "Aaron":
if name in ("Alexander", "Iryna", "Ihor", "Viktoriia", "Aaron"):
    print(name)
print("-" * 80)


# Task
"""
The all() function returns True if all items in an iterable are true, otherwise it returns False.
If the iterable object is empty, the all() function also returns True.
The any() function returns True if any item in an iterable are true, otherwise it returns False.
If the iterable object is empty, the any() function will return False.
"""
a = b = c = d = e = True
# if a and b and c and d and e:
if all((a, b, c, d, e)):
    print("All True")
if any((a, b, c, d, e)):
    print("Any True")
print("-" * 80)


# Task
"""
The ternary operator is a way of writing conditional statements in Python. As the name ternary suggests, 
this Python operator consists of three operands. The ternary operator can be thought of as a simplified, 
one-line version of the if-else statement to test a condition.

value_if_true if condition else value_if_false
"""
age = 30
ticket_price = 20 if int(age) >= 18 else 5
print(f"The ticket price is {ticket_price}")
print("-" * 80)


# Task
"""
Configure dictionary
"""
class User:
    def __init__(self, group: str):
        self.group = group
user = User(group="admin")
# if user.group == "admin":
#     process_admin_request(user, request)
# elif user.group == "manager":
#     process_manager_request(user, request)
# elif user.group == "client":
#     process_client_request(user, request)

group_to_process = {  # here we are doing setting
    "admin": process_admin_request,
    "manager": process_manager_request,
    "client": process_client_request,
}
group_to_process_method[user.group](user, request)  # here we are doing programming
print("-" * 80)


# Task
"""
A lambda function is a small anonymous function. A lambda function can take any number of arguments, but can only 
have one expression.
"""
ages = [33, 90, 17, 15, 21, 60, 5]
adults = list(filter(lambda age: age >= 18, ages))
print(adults)
print("-" * 80)