def power(a,b):
    p=1
    i=1
    while(i<=b):
        p=p*a
        i=i+1
    return p
    
#main start
a=int(input("Enter base "))
b=int(input("Enter index "))
z=power(a,b)
print(z)


#accept the number and check is it prime or not using user defined function
