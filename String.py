'''a = "Harry Potter"
print(a)
print(len(a))
print(a.count("r"))
print(a.upper())
print(a.lower())
print(a.index("r"))
print(a.capitalize())
print(a.casefold())
print(a.find("o"))

name = "John"
print(name.center(20,"*"))

age = 21
x = "my name is {}, my age is {}"
print(x.format(name,age))'''

#Problems

#Q.1 Take an input from a user as a string then reverse it.
'''a = input("enter anything here: ")
print(a[::-1])'''

#Q.2 Write a program to check if a string contains only digits.
'''a = input("enter anything here: ")
b = (a.isdigit())
if b == True:
    print("it contains only digits")
else:
    print("it does not contain only digits")'''

#Q.3 Write a program to check if a string is palindrome.
'''a = input("enter anything here: ")
rev = a[::-1]

if a == rev:
    print("it is a palindrome")
else:
    print("it is not palindrome")'''

#Q.4 Write a program to find number of vowels in a string.
'''a = input("enter anything here: ")
vowels = 0
for i in a:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
        vowels += 1
print("the number of vowels in the following string are",vowels)'''

#Q.5 Write a program to check if every word in a string begins with a capital letter.
a = input("enter anything here: ")
print(a.istitle())



