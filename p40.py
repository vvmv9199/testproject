def fact(n):
    f=1
    while(n>=1):
        f=f*n
        n=n-1
        return(f)

    i=1
    s=1
    n=int(input("enter any no"))
    while(i<=n):
     s=s+1/fact(i)
     i=i+1
    print("sum of series=",s)
