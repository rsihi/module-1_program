# Write a Python program to count occurrences of a substring in a string.

x=input("Enter your string : ")
z=x.split()

for i in z:
    print(i,end=" : ")
    print(z.count(i))