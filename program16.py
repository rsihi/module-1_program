#  Write a Python program to find the first appearance of the substring 'not'
#  and 'poor' froma given string, if 'not' follows the 'poor', replace the whole
# 'not'...'poor'substring with 'good'. Return the resulting string

x=input("Enter your string: ")

y=x.replace("not poor","good")

print(y)