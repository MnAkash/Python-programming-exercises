# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

input_str = input()
dimensions = [int(x) for x in input_str.split(',')]

row = dimensions[0]
col = dimensions[1]

# conventional method
array = [[0 for i in range(0, col)] for j in range(0, row)]
for i in range(0, row):
    for j in range(0, col):
        array[i][j] = i * j

# using list comprehension
multilist = [i * j for i in range(0, col)] for j in range(0, row)]

print(array)
print(multilist)
