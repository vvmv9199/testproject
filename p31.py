def divfun(a,b):
    c=a/b
    print("Division:",c)

def divfun1(a,b):
    c=a/b
    return c


 #main start

x=int(input("Enter any number"))
y=int(input("Enter second number"))
divfun(x,y)
z=divfun1(x,y)
print(z)
