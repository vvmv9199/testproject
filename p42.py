def summation(n):
    i=1
    s=0
    while(i<=n):
        s=s+i
        i=i+1
    return(s)
#main start
i=0
s=0
n=int(input("Enter value for n"))
while(i<=n):
    i=i+1
    s=s+1/summation(i)

print("sum of series=",s)

