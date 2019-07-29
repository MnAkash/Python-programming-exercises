'''
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200
'''

# computes net bank amount based on the input
# "D" for deposit, "W" for withdrawal 

net_amount = 0

while True:	 
	str = input ("Enter transaction: ")# input the transaction
	
	transaction = str.split(" ")# seprated by space

	# get the value of transaction type and amount in the separated variables
	type = transaction [0]
	amount = int (transaction [1])

	if type=="D" or type=="d":
		net_amount += amount

	elif type=="W" or type=="w":
		net_amount -= amount
	else:
		pass

	str = input ("Want to continue (Y for yes) : ") #input choice
	if not (str[0] =="Y" or str[0] =="y") :
		break

print ("Net amount: ", net_amount)