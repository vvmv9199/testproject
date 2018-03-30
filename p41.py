def fact(n):
    f=1
    while(n>1):
        f=f*n
        n=n-1
    return(f)


#main start
i=1
s=0
n=int(input("enter any number"))
while(i<=n):
 s=s+(i+1)/fact(i)
 i=i+1
print("sum of series=",s)
