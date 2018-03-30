#def max(a,b,c):
#   m=0
#    if(a>b):
#      m=a
#    else:
#      m=b
#    if(c>m):
#      m=c
#    print("Maximum number:",m)
#    return(m)

def getmax(a,b):
    if(a>b):
        return a
    else:
        return b


a=int(input("Enter any number"))
b=int(input("Enter second number"))
c=int(input("Enter third number"))
mm=getmax(a,b)
mm=getmax(c,getmax(a,b))
print("Maximum number;",mm)         
