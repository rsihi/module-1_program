#  Write a Python function that takes a list of words and returns the length
#  of the longest one.

x=[]
n=int(input("Enter your no of string : "))

for i in range(n):
    a=input("Enter your String : ")
    x.append(a)
    


def long():
    longest=x[0]
    for i in x:
        if len(longest)<len(i):
            longest=i
    print(f"{longest} : {len(longest)}")


long()
        
        