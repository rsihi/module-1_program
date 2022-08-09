# Write a Python program to count the occurrences of each word in a given
# sentence  

x=input("Enter your string : ")
z=x.split()
for i in z:
    print(f"{i} : {z.count(i)}")
    
       