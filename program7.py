#  Write a Python program to sum of three given integers.However, if two
#  values are equal sum will be zero.

a=int(input("Enter your First value : "))
b=int(input("Enter your second value : "))
c=int(input("Enter your third value : "))

if a==b or a==c or b==c:
    print("Your sum is 0")
else:
    print("Sum : ",a+b+c)
    
    