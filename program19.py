#  Write a Python program to get a string made of the first 2 and the last 2
#  chars from a given a string. Ifthe string length islessthan 2,return instead
#  of the empty string.

x=input("Enter your string : ")

if len(x)>=2:
    print(x[:2]+x[-2:])