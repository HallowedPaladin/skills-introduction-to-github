"""
This file contains the code for the Week 3 lab exercises,
focusing on for loops, while loops, and GitHub integration.
"""
#this is a for loop that counts up from 1 to 20 in only even numbers
for i in range(1, 20, 2):
    print(i+1)
     
#this is a for loop that gets the sum of a list and prints the result
collectiveiqGomdi = [2.7, 60.0, 90.0, 140.0, 110.0, 110.1]
totaliq = 0
for iq in collectiveiqGomdi:
    totaliq = totaliq + iq
print(f"\n The collective IQ of gomdi is {totaliq:.1f}")

#this is a nested for loop for creating shapes (right angled triangles)
for i in range(5):
    for i in range (i+1):
        print("*",end=' ')
    print()

choice = ''

while choice == '':
    print("1. Add\n2. Subtract\nq. Quit")
    choice = input()
    choice = int(choice)

    if choice == 1:
        value1 = 0
        value2 = 0
        result = 0
        value1 = input("What is the first value?\n")
        value2 = input("What is the second value?\n")
        result = value1 + value2
        print(f"Your sum is: {result:.1f}")
