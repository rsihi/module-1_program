# Write a Python program to count the number of characters (character
# frequency) in a string

x=input("Enter your string :  ")

for i in x:
    print(i,end=":")
    print(x.count(i))