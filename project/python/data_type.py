
# simple calculator
# addition, division, multiplication, subtraction
# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# sum = float(num1) + float(num2)
# division = float(num1) / float(num2)
# multiplication = float(num1) * float(num2)
# subtraction = float(num1) - float(num2)
# print("sum :" , sum)
# print("division :" , division)
# print("multiplication :", multiplication)
# print("subtraction :", subtraction)

# a = True
# b = False
# if a!=b :
#     print("a is not equal to b")
# elif a==b :
#     print("a is equal to b")
# else:
#     print("a is greater than b")
# print("watch for the output...")

# result = not b
# print( result)

#nested condition.........
# year = int(input("Enter a year: "))

# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print(year, "this is a leap year")
#         else:
#             print(year, "this is not a leap year")
#     else:
#         print(year, "this is not a leap year")
# else:
#     print(year, "this is not a leap year")   

# first_number = float(input("Enter a Number: "))
# second_number = float(input("Enter another Number: "))
# operations = input("Enter an operation (+, -, *, /): ")

# if operations == "+":
#     result = first_number + second_number
# elif operations == "-":
#     if first_number < second_number:
#         print("Error: Cannot subtract a larger number from a smaller number.")
#     else:
#         result = first_number - second_number
# elif operations == "*":
#     result = first_number * second_number
# elif operations == "/":
#     if second_number == 0:
#         print("Error: Division by zero is not allowed.")
#     else:
#         result = first_number / second_number
# else:
#     print("Result: Invalid operation.")
    
    
    
# Determine the ticket price based on the age of the customer.
'''from itertools import count
age = int(input("Enter your Age : "))
is_student = input("Are you a student? (yes/no): ").lower()
is_veteran = input("Are you a veteran? (yes/no): ").lower()
if age >= 61:
    if is_veteran == "yes":
        print("Ticket price is 7$/hr.")
    else:
      print("Ticket price is free.")
elif age >= 8 and age <= 25:
    if is_veteran == "yes" and is_student == "yes":
            print("Ticket price is 0.00 $/hr.")
    elif is_student == "no" or is_veteran == "yes":
        print("Ticket price is 3$/hr.")
    else:
        print("Ticket price is 5$/hr.")
elif age >= 26 and age <= 60:
    if is_student == "no" and is_veteran == "yes":
        print("Ticket price is 1$/hr.")
    else:
        print("Ticket price is 10$/hr.")
elif age >= 61:
        print("Ticket price is 7$/hr.")
else:
        print("Invalid age.")
print("Thank you for your purchase.")
    '''
'''
count = int(input("Enter a number: "))
while count <5:
    print(count)
    count +=1
'''
## Conditional loop

             # break statement
'''
x = int(input("Enter a number: "))
for i in range(x):
    if i == 13:
        break
    print(i, end=" ")
    
else:
    print("The loop completed successfully.")
'''
                # continue statement----Flow Control
'''
for i in range(10):
    if i%2==1:
        continue
    print(i, end=" ")
'''

               # pass statement (do nothing)
'''
for i in range(10):
    if i == 5:
        pass
    print(i, end=" ")
'''
            # Nested loop
            
'''for i in range(4):
    for j in range(3):
      # print(i, j, end=" ")
      print(f"i={i}, j={j}")'''
      
     # sum of first 10 natural numbers    
'''num=10
sum=0
count=1
while count<=num:
    sum=sum+count
    count=count+1
print("The sum is", sum)
'''

'''num =10
sum =0
for i in range(11):
    sum+=i
print("The sum is", sum)
'''
# print the multiplication table of a number
'''num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num*i)
    '''
    

'''num = int(input("Enter a number: "))
i = 1
while i <=10:
    print(num, "X", i, "=", num*i)
    i+=1
    '''
    # prime numbers between 1 to 100
    # along with for loop you can use else statement
    
'''for i in range(1, 101):
        if i>1:
            for j in range(2, i):
               if i%j==0:
                   break
            else:
                print(i, end=" ") 
                '''
                
                
'''str = "abhijith.as"
str1 = "hello iam"
print(str.split(".")[0])
print(str.upper())
print(str.count("a"))
print(len(str))
print(str1 + " " + str)
print(str.replace("abhijith.as", "Lucifer"))
print(str.find("l"))
substring = "as"
if substring in str:
    print(substring, "found")

text = "       hey there how are you       "
print(text.strip())
print(text.lstrip())
print(text.split()) '''

# Regular expressions...........

# Match V/S Search
'''re.match() function only checks for a match at the beginning of the string, 
while re.search() checks for a match anywhere in the string.'''

# Search....
'''import re

text = "The rain in Spain"
pattern = "ain"
search = re.search(pattern, text)
if search:
    print("Match found", search.group())
else:
    print("Match not found") '''
        
# Match.....

'''Uses when dealing with "Error messages, Logs, Warning messages, etc."'''
'''import re

text =  "Error: The password is incorrect."
pattern = "Error"
match = re.match(pattern, text)
if match:
    print("Match found", match.group())
else:
    print("Match not found")
    '''

'''  
x = 10
y = 20

def add():
    add = x + y
    print(add)
def sub():
    sub = x - y 
    print(sub)
def mul():
    mul = x * y
    print(mul) 
def div():  
    div = x / y
    print(div)
    
 # calling the functions   
add()
sub()
mul()
div()
'''

# Other ways.....BETTER WAY---improve the code, reasability, maintainability, Reusability

def add(x, y):
    add = x + y
    return add
def sub(x, y):
    sub = x - y 
    return sub
def mul(x, y):
    mul = x * y
    return mul 
def div(x, y): 
    try:
        div = x / y
    except ZeroDivisionError as ze :
        print("Zero Division Error")
        return None
    else:
        return div
# floor division---Resource utilization / RAM--rounding off the value
def float_div(x, y):
    float_div = x // y
    return float_div
    
 # calling the functions   
print(add(5, 10))
print(sub(10, 5))
print(mul(10, 10))
print(div(7, 2))
print(float_div(7, 2))
 
