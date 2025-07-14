#Q.1 Write a program to check if a number is positive.
'''num = int(input("enter a number: "))
if num > 0:
    print("It is positive")'''

#Q.2 Write a program to check whether a number is odd or even
'''num = int(input("enter a number: "))
if num % 2 == 0:
    print("It is an even number")
else:
    print("It is an odd numver")'''
    
#Q.3 Write a program to create area calculator
'''print("**********Area Calculator**********")

print("""press 1 to get area of square
press 2 to get the area of rectangle
press 3 to get the area of circle
press 4 to get the area of triangle""")

choice = int(input("enter a number between 1 t0 4: "))

if choice == 1:
    side = float(input("enter the length of one side: "))
    area = side * side #side**2
    print("the area of square is ",area)
elif choice == 2:
    length = float(input("enter the length of the rectangle: "))
    width = float(input("enter the width of the rectangle: "))
    area = length * width
    print("the area of rectangle is: ",area)
elif choice == 3:
    radius = float(input("enter the radius of the circle: "))
    area = ((22/7) * (radius**2))
    print("the area of the circle is: ",area)
elif choice == 4:
    base = float(input("enter the base of the triangle: "))
    height = float(input("enter the height of the height: "))
    area = 0.5 * base * height
    print("the area of triangle is: ",area)
else:
    print("Invalid choice :)")'''
    
#Q.4 Write a program check whether the passed letter is a vowel or not.
'''letter = input("enter the letter here: ")
if (letter in "aeiou") or (letter in "AEIOU"):
    print("it is a vowel")
else:
    print("it is not a vowel")'''
    

#Q.5 write a program to check if a number is sinle digit number,
#2-digit number and so on.. up to 5 digits.

num = int(input("enter a number here up to 5 digits: "))
if num >= 0 and num <= 9:
    print("it is a single digit number")
elif num >= 10 and num <= 99:
    print("it is a double digit number")
elif num >= 100 and num <= 999:
    print("it is a triple digit number")
elif num >= 1000 and num <= 9999:
    print("it is a four digit number")
else:
    print("it is a five digit number")
