a=["RAM","SHYAM","RANI","RAJU"]
ans='y'
while(ans=='y'):
    rno=int(input("enter roll no from 1 to 4"))
    if(rno<0 or rno>4):
        print("invalid roll no")
    else:
        print("Name is ",a[rno-1])
    ans=input("Want to continue??")
