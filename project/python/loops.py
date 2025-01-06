'''for i in range(1, 11):
    print(i)
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
'''

'''colours = ["red", "green", "blue", "yellow"]
for i in range(10):
    print(colours)
    print(i)'''
    
'''while True:
    print("hello world") 
    break'''
    
# numbers = [1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,14,15]
# for num in numbers:
#     if num%2==0:
#         continue
#     print(num)

import argparse
parser = argparse.ArgumentParser(description="Process some integers.")
parser.add_argument('--integer', required=True,type=int, help='please provide the integer')
args = parser.parse_args()
if args.integer % 2 ==0:
    print(f"{args.integer} is even")
else:
    print(f"{args.integer} is odd")