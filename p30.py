def addfun(a,b): #non returning value function (void function)
    c=a+b
    print("Addition",c)

def addfun1(a,b): #returning value function (int.float,char returns from function)
    c=a+b
    return c

#main start
    
x=int(input("Enter first number"))
y=int(input("Enter second number"))
addfun(x,y)
z=addfun1(x,y)
print(z)
