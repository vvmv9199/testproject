no=0
a=int(input("enter any number"))
x=a
#now for palindrome
while (a>0):
    r=a%10
    no=no*10+r
    a=a//10
    print(no)
if(x==no):
    print("it is palindrome")
else:
    print("it is not a palindrome")
    
