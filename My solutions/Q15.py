#Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

a=input('Enter a number:')

b=int(a)+int(a+a)+int(a+a+a)+int(a+a+a+a)

print(b)