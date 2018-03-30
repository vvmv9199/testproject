nm=["RAM","SHYAM","RANI","RAJU"]
rno=[10,20,30,40]
marks=[560,230,400,360]

ans='y'
while(ans=='y'):
    flag=0
    no=int(input("Enter the roll number"))
    for i in range(0,len(rno)):
       if(no==rno[i]):
           print("Name is ",nm[i])
           print("Marks are ",marks[i])
           flag=1
           break
    if(flag==0):
        print("Please check for roll no")
    ans=input("Want to try again??")
        
