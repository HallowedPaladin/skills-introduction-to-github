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