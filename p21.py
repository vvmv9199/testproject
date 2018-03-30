no=int(input("Enter meter number"))
nm=input("Enter consumer name")
cr=int(input("Enter current reading"))
pr=int(input("Enter previous reading"))
nt=pr+cr
if(nt<=100):
    ch=3.5*100
else:
    ch=(3.5*100)+(nt-100)*7.5
print("Total charges",ch)
