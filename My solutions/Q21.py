'''
A robot moves in a plane starting from the origin point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
The numbers after the direction are steps.
Please write a program to compute the distance from current position after a sequence of movement and original point.
If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2
'''
from math import sqrt
updown_dist=0
leftright_dist=0

while True:	 
	str = input ("Enter movement: ")
	
	movement = str.split(" ")

	type = movement [0]
	dist = int (movement [1])

	if type=="DOWN":
		updown_dist += dist
	elif type=="UP":
		updown_dist -= dist

	elif type=="LEFT":
		leftright_dist += dist
	elif type=="RIGHT":
		leftright_dist -= dist

	str = input ("Continue?(y/n):")
	if not (str[0] =="Y" or str[0] =="y") :
		break
		
#print(updown_dist,leftright_dist)
approx_pythagorian_dist=round(sqrt(updown_dist**2+leftright_dist**2))
print ("\nApprox Pythagorian Distancee: ", approx_pythagorian_dist)