ary=[]
for i in range(0,5):
    n=input("Enter any word")
    ary.append(n)
print(ary)

ans='y'
while(ans=='y'):
    n=input("Enter any word")
    ary.append(n)
    ans=input("Want to continue??")

print(ary)
