
# Question 1(i)
# Write a Python program to find the distance between two 
# coordinate points (x1, y1) and (x2, y2).
x1 = int(input("Enter the value of x1:\t "))
x2 = int(input("Enter the value of x2:\t"))
y1 = int(input("Enter the value of y1:\t "))
y2 = int(input("Enter the value of y2:\t"))
 
import math

distance = ((x2-x1)**2 +(y1-y2))**2
d = math.sqrt(distance)
print(d)

# Question 1(ii)
# Write a Python program to find maximum between three numbers.
def maximum_numbers():

    numbers = [1,4,9]
    numbers.append(max)
    print(numbers)
maximum_numbers()



