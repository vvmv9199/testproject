def fact(n):
    f=1
    while(n>1):
        f=f*n
        n=n-1
    return (f)

 
i=1
s=0
n=int(input("enter any no "))
while i<=n:
   s=s+1/fact(i)
   i=i+1
   
print("sum of series =",s)



      #9326019610

      #mujumdar
      #9322271966


#1+1/2!+1/3!+1/4!....1/n!
