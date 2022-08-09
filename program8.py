#  Write a Python program that will return true ifthe two given integervalues
#  are equal or their sum or difference is 5.

a=int(input("Enter your First value : "))
b=int(input("Enter your second value : "))

if a==b or a+b==5 or a-b==5:
    print(True)