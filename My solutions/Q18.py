'''
Quesation:
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
'''
output=[]

Input=input('Enter passwords separated with comma\n')
Input=Input.split(",")
print('Usable passwords are:')

for i in range(len(Input)):
	alpha_lower=0
	alpha_upper=0
	numeric=0
	special=0
	for j in Input[i]:

		if j.isalpha():
			if(j.islower()):
				alpha_lower +=1
			else:
				alpha_upper +=1

		elif j.isnumeric():
			numeric +=1

		elif j=='$' or j=='#' or j=='@':
			special +=1

		else:
			pass

	if alpha_upper>0 and alpha_lower>0 and numeric>0 and special>0 and (5<len(Input[i])<13):
		#print(Input[i],end=',')
		output.append(Input[i])

print(','.join(k for k in output))