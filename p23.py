d=0
a=int(input("enter any number"))
x=a
#if (a<10):
#   d=1
#elif(d<100):
#    d=2
#elif(d<1000):
#    d=3
#elif(d<10000):
#d=4
while x>0:
    x=x//10
    d=d+1

print(a," is of ",d," digits")
#now for armstrong no
x=a
s=0
while x>0:
    r=x%10
    s=s+pow(r,d)
    x=x//10;
if(s==a):
    print("it is armstrong no ")
else:
    print("it is not an armstrong no")
    




    
