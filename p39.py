#accept the number and check whether is it prime or not using user defined function
def prime(n):
    d=2
    while(d<=n//2):
        if(n%d==0):
            return 0
        d=d+1
    return 1
    

    


#main start
ans='yes'
while(ans=='yes'):
    n=int(input("Enter any number"))
    if(n==0 or n==1):
        print("neither prime nor composite")
    elif(n==2):
        print("It is prime")
    else:
        if(prime(n)==1):
            print("It is prime ")
        else:
            print("It is composite")
    ans=input("continue??")
    
        
        
