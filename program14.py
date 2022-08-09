#  Write a Python program to get a single string from two given strings,
#  separated by a space and swap the first two characters of each string.

x=input("Enter your string : ")
y=input("Enter your string : ")

x1=y[:2]+x[2:]
y1=x[:2]+y[2:]

print(x1,end=" ")
print(y1)