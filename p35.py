def max(a,b,c):
    m=0
    if(a>b):
     m=0
    else:
     m=b
    if(c>m):
     m=c
    return(m)
a=int(input("Enter any no:"))
b=int(input("Enter second number;"))
c=int(input("Enter third number:"))
mm=max(a,b,c)
print("Maximum number:",mm)
