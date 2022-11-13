# Task
"""
Find a sum of the entered numbers
"""
a = 235
s = 0
while a > 0:
    s += a % 10  # because of decimal number system
    a = a // 10
print(s)
print("-" * 80)


# Task
"""
You have a list of numbers. Turn it to the list of numbers powered in two(squared)
"""
list = [7, 8, 4, 10, 5, 9]
new_list = []
for i in list:
    new_list.append(i ** 2)
print(new_list)

new_list2 = [i ** 2 for i in list]  # list comprehension
print(new_list2)
print("-" * 80)


# Task
"""
You have a string with words and spaces. Find a quantity of words in string
"""
s = "Some string with spaces"
k = 0
for i in s:
    if i == " ":
        k += 1
print(k + 1)

print(len(s.split()))
print("-" * 80)


# Task
"""
Make a calculator of lucky numbers. You should find a sum of the numbers of your date birthday
"""
s = "1990.12.25"
s1 = s.split(".")
year = int(s1[0])
month = int(s1[1])
day = int(s1[2])
sum = 0
while year > 0:
    sum += year % 10
    year //= 10
while month > 0:
    sum += month % 10
    month //= 10
while day > 0:
    sum += day % 10
    day //= 10
sum1 = 0
while sum > 0:
    sum1 += sum % 10
    sum //= 10
print(sum1)
print("-" * 80)


# Task
"""
You have a string. Find the number(count) of vowels in the given string.
a, e, i, o, u consider as vowels, but not y.
"""
def count(string):
    return len([i for i in string if i in "aeiouAEIOU"])
print(count("You have a string"))
print("-" * 80)


# Task
"""
Write a function that takes a string and return a new string with all vowels removed.
a, e, i, o, u consider as vowels, but not y.
"""
def newString(string):
    return "".join([i for i in string if i not in "aeiouAEIOU"])
print(newString("Write a function that"))
print("-" * 80)


# Task
"""
Write a function that square every digit of a number and concatenate them
"""
def square_digits(number):
    return int("".join([str(int(i) ** 2) for i in str(number)]))
print(square_digits(426))
print("-" * 80)


# Task
"""
You are given a string of space separated numbers. Return the highest and lowest number
"""
def result(numbers):
    numbers = [int(i) for i in numbers.split()]
    return " ".join([str(max(numbers)), str(min(numbers))])
print(result("3 4 6 -3 6 10 4"))
print("-" * 80)


# Task
"""
Rearrange the digits in given number to create the highest possible number
"""
def order(number):
    return int("".join(sorted([i for i in str(number)], reverse=True)))
print(order(245365))
print("-" * 80)


# Task
"""
Write a function that transforms given string like in example: "abcd" -> "A-Bb-Ccc-Dddd"
"""
def function(s):
    return "-".join([s[i].upper() + (s[i].lower() * i) for i in range(len(s))])
print(function("abcde"))
print("-" * 80)


# Task
"""
You have a word. You need to return the middle character of the word.
If the word's length is odd, return the middle character. If it's even - return the middle 2 characters
"""
def middle(s):
    if len(s) % 2:
        return s[len(s) // 2]
    else:
        return s[len(s) // 2 - 1:len(s) // 2 + 1]
print(middle("word"))
print(middle("results"))
print("-" * 80)


# Task
"""
In the given number determine if it is a square number
"""
def square(n):
    return True if n > -1 and n ** 0.5 == int(n ** 0.5) else False
print(square(64))
print(square(25))
print(square(26))
print("-" * 80)


# Task
"""
In the given list that contains both integers and strings, return new list with the strings filtered out
"""
def filter(list):
    return [i for i in list if type(i) is int]
print(filter([1, 2, 4, "afde", "sfd"]))
print("-" * 80)


# Task
"""
Write a function that determines whether a string that contains only letters is an isogram.
Isogram is a word that has no repeating letters, consecutive or non-consecutive
Hint:
You can remove duplicates from a Python using the list(dict.fromkeys(x)), which generates a dictionary 
that removes any duplicate values. You can also convert a list to a set. 
You must convert the dictionary or set back into a list to see a list whose duplicates have been removed
"""
def isogram(string):
    return True if len(set(string.lower())) == len(string.lower()) else False
print(isogram("aba"))
print(isogram("abd"))
print("-" * 80)


# Task
"""
Convert strings capitalizing every word 
"""
def case(string):
    return " ".join([i.capitalize() for i in string.split()])
print(case("simple test text is here"))
print("-" * 80)


# Task
"""
In a given string of words, return the length of the shortest word
"""
def shortest(s):
    return min([len(i) for i in s.split()])
print(shortest("lets talk about python the best language"))
print("-" * 80)


# Task
"""
Replace all symbols "A" on "T", and "C" on "G"
Let's use dictionary 
"""
def replace(s):
    return "".join([{"A": "T", "T": "A", "C": "G", "G": "C"}[i] for i in s])
print(replace("CATG"))
print("-" * 80)


# Task
"""
Check to see if the string has the same amount of chars
"""
def same(s):
    return True if s.lower().count("x") == s.lower().count("o") else False
print(same("xxo"))
print("-" * 80)


# Task
"""
Write a function which changes all but the last four characters into "#" 
"""
def masked(c):
    return (len(c) - 4) * "#" + c[-4:]
print(masked("k2j3hg4k2g5h2b524523"))
print(masked("k2j3h523"))
print("-" * 80)


# Task
"""
Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, containing distinct 
letters - each taken only once - coming from s1 or s2
"""
def longest(s1, s2):
    return "".join(sorted(set(s1) | set(s2)))
s1 = "sdgfsfewfhgj"
s2 = "edfrh"
print(longest(s1, s2))
print("-" * 80)