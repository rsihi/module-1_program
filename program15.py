#   Write a Python program to add 'ing' at the end of a given string (length
#   should be at least 3). If the given string already ends with 'ing' then add 'ly'
#   insteadif the string length of the given string is less than 3, leave it
#   unchanged.

x=input("Enter your string : ")

if len(x)>=3:
    if x[-3:]=="ing":
        print(x+"ly")
    else:
        print(x+"ing")
else:
    print(x)