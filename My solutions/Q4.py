'''
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
'''
Input=input('Enter numbers seperated with comma:\n')
Input=Input.split(',')
print(Input)
'''
TupInput=()                     #TupInput = tuple(Input) -er bikolpo
for i in range(len(Input)):
	TupInput = TupInput + (Input[i],)
'''
TupInput = tuple(Input)
print(TupInput)
