def max(a,b,c):
    m=0
    if(a>b):
     m=a
    else:
     m=b
    if(c>m):
     m=c
    return(m)
a=int(input("Enter any number"))
b=int(input("Enter second number"))
c=int(input("enter third number"))
mm=max(a,b,c)
print("Maximum number",mm)
