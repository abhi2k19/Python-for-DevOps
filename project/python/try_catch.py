import os

'''try:
    file = open('loops.py', 'r')
    print(file.read())
except FileNotFoundError:
    print("File not found")
else:
    print("...openend in read mood")
    file.close()
finally:
    print("...closed") '''


folders = input("Enter the folder name: ").split()
for folder in folders:
    try:
        files  =  os.listdir(folder)
       # print("listing files" , files)
    except FileNotFoundError:
        print("Please enter a valid folder name :"+ " " + folder) 
        continue
    except PermissionError:
        print("Permission denied for folder: " + folder)
    for file in files:
        print(folder ,  file)
#-----------------------------------------------------------------------------        
num1 = float(input("Enter the first number: "))
num2 =  float(input("Enter the second number: "))
try:
    div = num1/num2
    print(div)
except ZeroDivisionError:
    print("Cannot divide by zero")
