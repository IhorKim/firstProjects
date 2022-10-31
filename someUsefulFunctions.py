# List of some interesting useful functions
print('Bubble Sort Algorithm')
list = [4, 5, 7, 9, 0, 3, 2, 1, 6, 8]
def bubbleSort(seq):
    n = len(seq)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if seq[j] > seq[j + 1]:
                value = seq[j]
                seq[j] = seq[j + 1]
                seq[j + 1] = value
    return seq
print(bubbleSort(list))
print('-' * 70)


print('Sort elements in list')
list = [4, 5, 7, 9, 0, 3, 2, 1, 6, 8]
list.sort()
print(list)
list.sort(reverse=True)
print(list)
print('-' * 70)


print('Sort elements in list')
list = [4, 5, 7, 9, 0, 3, 2, 1, 6, 8]
newList = []
while list:
    min = list[0]
    for i in list:
        if i > min:
            min = i
    newList.append(min)
    list.remove(min)
print(newList)
print('-' * 70)


print('Print prime numbers between 50 and 100')
for number in range(50, 100):
    if all(number % i != 0 for i in range(2, number)):
        print(number)
print('-' * 70)


print('Fibonacci series')
def Fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fib(n - 1) + Fib(n - 2)
for i in range(0, 20):
    print(Fib(i))
print('-' * 70)


print('Palindrome')
def isPalindrome(s):
    rev = ''.join(reversed(s))
    if s == rev:
        return True
    return False
print(isPalindrome('madam'))
print('-' * 70)


print('Duplicates in list')
list = [4, 5, 3, 6, 8, 7, 9, 0, 3, 2, 1, 6, 8]
print(set([i for i in list if list.count(i) > 1]))
print('-' * 70)


print('Reverse a list')
list = [4, 5, 3, 6, 8, 7, 9, 0, 3, 2, 1, 6, 8]
def rev(l):
    return l[::-1]
print(rev(list))
print('-' * 70)


print('Extract digits from string')
testString = 'ojnsdf7896s7fer3hbu'
result = ''.join(filter(lambda i: i.isdigit(), testString))
print(result)
print('-' * 70)


print('Delete reoccuring characters')
def delete(s):
    seenCharacters = set()
    outputString = ''
    for char in s:
        if char not in seenCharacters:
            seenCharacters.add(char)
            outputString += char
    return outputString
print(delete('sssffgfhhkktbeddv'))
print('-' * 70)


print('FizzBuzz')
counter = 0
for i in range(1, 51):
    if i % 5 == 0 and i % 3 == 0:
        print('FizzBuzz')
        counter += 1
    elif i % 3 == 0:
        print('Fizz')
        counter += 2
    elif i % 5 == 0:
        print('Buzz')
        counter += 3
    else:
        print(i)
print(counter)
print('-' * 70)





