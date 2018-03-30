pm=int(input("Enter principal amount"))
pd=int(input("Enter period of deposit"))
rt=int(input("Enter rate of interest"))

i=0
brk=0
s=0
while i<=pd:
   i=i+1
   brk=1+rt/100;
   s=s+pow(brk,i)
intr=s*pm
print("Amount on maturity ",intr)

