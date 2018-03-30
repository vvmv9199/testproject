a=["RAM","SHYAM","RANI","RAJU"]
found=0
n=input("Enter the name of the person")
for i in range(0,len(a)):
    if(a[i]==n):
        print("available")
        found=1
        break
    
if(found==0):
    print("unavailble")

