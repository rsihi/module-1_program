# Write python program that swap two number with temp variable and
# without temp variable.

# with tmp variabel.

a=int(input("Enter your a number : "))
b=int(input("Enter Your b number : "))

tmp=a
a=b
b=tmp

print("a : ",a)
print("b : ",b)

#without tmp variabel 
a=int(input("Enter your a number : "))
b=int(input("Enter Your b number : "))

a=a+b
b=a-b
a=a-b

print("a : ",a)
print("b : ",b)