# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
arr=[]
for value in range(2000,3201):
    if value%7==0 and value%5!=0:
        arr.append(value)
print(','.join(str(i) for i in arr)) #this join operation only works with string type