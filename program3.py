# Write a Python program to get the Fibonacci series of given range.

n=int(input("Enter Your range : "))
a=0
b=1
c=1
for i in range(n):
    print(a)
    a=b
    b=c
    c=a+b

