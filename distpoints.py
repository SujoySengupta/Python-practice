#. Write a program to compute distance between two points accepted from the 
#user. 
import math
x1=int(input("Enter x-coordinate of first point: "))
y1=int(input('Enter y-coordinate of first point: '))
x2=int(input("Enter x-coordinate of second point: "))
y2=int(input('Enter y-coordinate of second point: '))
dist=math.sqrt((x2-x1)**2 + (y2-y1)**2)
print("the distance between the two points are ",dist,'units')
