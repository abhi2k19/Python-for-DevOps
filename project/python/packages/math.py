def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

'''today = input("Enter the date: ").strip().lower()
if today == "monday":
    print("Today is Monday")
elif today == "tuesday":
    print("Today is Tuesday")
else:
    print("Today is neither Monday nor Tuesday")'''
    
import argparse

parser = argparse.ArgumentParser(description="An Ec2 instance creator")
parser.add_argument("--instance_type", help="Enter the instance type", required=True)
parser.add_argument("--instance_name", help="Enter the instance name", required=True)
parser.add_argument("--region", help="Enter the region", required=True)
args = parser.parse_args()
if args.instance_type == "t2.micro":
    print("Eligible for free tier")
else:
    print("Not eligible for free tier")

print(f"created instance is of '{args.instance_type}' type and named as '{args.instance_name}' in the region '{args.region}'")