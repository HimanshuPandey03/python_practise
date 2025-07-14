#Q.1 Write a program to get Fibonacci series up to 10  numbers.
'''a = 0
b = 1
n = int(input("Enter a number here: "))
if n == 1:
    print(1)
else:
    print(a)
    print(b)
    for i in range(2,n):
        c = a + b
        a = b
        b = c
        print(c)'''

#Q.2 Write a program to check if a number is prime or not.
'''num = int(input("enter a number here: "))
if num <= 1:
    print("it is not a prime number")
else:
    for i in range(2,num):
        if num % i == 0:
            print("it is not a prime number")
            break
        else:
            print("it is a prime number")'''
        
#Q.3 Write a program to find a palindrome of integers.
num = int(input("enter a number here: "))
temp = num
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
    
if rev == temp:
    print("it is palindrome")
else:
    print("it is not a palindrome")

