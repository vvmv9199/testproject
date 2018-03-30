def power(a,b):
    p=1
    i=1
    while(i<=b):
        p=p*a
        i=i+1
    return p

#main start
i=1
s=0
n=int(input("enter any no "))
while(i<=n):
    x=power(i,i)
    s=s+(i+1)/x
    i=i+1
print(s)
 
