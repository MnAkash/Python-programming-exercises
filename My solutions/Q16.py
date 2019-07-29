'''
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,9,25,49,81
'''
Input=input('Enter numbers seperated with comma:\n')
Input=Input.split(',')

def is_odd(value):
	if value%2:
		return True
	else:
		return False

List=[]
for i in Input:
	if is_odd(int(i)):
		List.append(int(i)*int(i))

print(','.join(str(j) for j in List))