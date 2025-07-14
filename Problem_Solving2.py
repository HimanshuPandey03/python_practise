#Q.1 Write a program to find a sum of all the even numbers up to 50.
'''sum = 0
for i in range(0,51):
    if i % 2 == 0:
        sum += i
        print(i)
print("the sum of all the even number up to 50 is ",sum)'''

#Q.2 Write a program to wite first 20 numbers and their squared numbers.
'''for i in range(1,21):
    print(i,"square is ", i**2)'''

#Q.3 Write a program to find sum of first 10 odd numbers using while loop.
'''sum = 0
n = 0
while n <= 20:
    if n % 2 != 0:
        sum += n
    n += 1
print("the sum of first 10 odd number is ", sum)'''

#Q.4 Write a program to check if a number is diviible by 8 and 9 up to 100 numbers.
'''for i in range(1,101):
    if i % 8 == 0 and i % 9 == 0:
        print(i)'''
        

#Q.5 Write a program to create a billing system at supermarket.
'''while True:
    name = input("enter customer's name: ")
    total = 0
    while True:
        print("Enter the amount and quantity")
        amount = float(input("enter amount: "))
        quantity = float(input("enter quantity: "))
        total += amount * quantity
        repeat = input("do you want to add more items? (yes/no): ")
        if repeat == "no" or repeat == "No":
            break
    print("-"*40)
    print("Name: ",name)
    print("Amount to be paid: ", total)
    print("-"*40)
    print("**********Happy Shopping**********")

    repeat1 = input("do you want to go to next customer? (yes/no): ")
    if repeat1 == "no" or repeat1 == "No":
        break'''


'''a = "Why fit in, When you are Born to Stand Out!"
print(a)
#Q.1 Write a program to find the length of the following string.
print(len(a))

#Q.2 Write a program to check how many time alphabet o is occurring.
print("the number of times o is occuring is: ",a.count("o"))

#Q.3 write a program to convert the whole string into lower and upper cases.
x = a.lower()
print(x)

y = a.upper()
print(y)

#Q.4 write a program to convert the following string into a title.
z = a.title()
print(z)

#Q.5 write a program to find the index number of "fit in".
print(a.find("fit in"))'''

#Q. Write a program to display this pattern.
'''1
1 2
1 2 3
1 2 3 4
1 2 3 4 5'''

'''for i in range(1,6): #rows
    for j in range(1,6): #columns
        print("*", end = " ")
    print()'''

'''for i in range(1,6): #rows
    for j in range(1,i+1): #columns
        print(j, end = " ")
    print()'''

#Q. Write a program to display this pattern.
'''1
2 2
3 3 3
4 4 4 4
5 5 5 5 5'''

'''for i in range(1,6): #rows
    for j in range(1,i+1): #columns
        print(i, end = " ")
    print()'''

#Q. Write a program to display this pattern.
'''1 1 1 1 1
2 2 2 2
3 3 3
4 4
5'''

'''for i in range(1,6): #rows
    for j in range(6, i, -1): #columns
        print("*", end = " ")
    print()'''

'''for i in range(1,6):
    for j in range(5, i, -1):
        print(" ",end = " ")
    for k in range(i):
        print("*", end = " ")
    print()'''


'''for i in range(1,6):
    for j in range(i, 0, -1):
        print(j, end = " ")
    print()'''


'''for i in range(1,6):
    for j in range(1,i+1):
        print("*", end = " ")
    print()
for i in range(5,0,-1):
    for k in range(0,i-1):
        print("*", end = " ")
    print()'''


'''for i in range(1,11):
    for j in range(1,i+1):
        print(i * j, end = " ")
    print()'''
        











    
    
    

