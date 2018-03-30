no=int(input("Enter worker no"))
nm=input("Enter worker name")
hr=float(input("Enter hours worked"))
if(hr<=8):
    wg=50*hr
else:
    wg=(8*50)+(hr-8)*90
print('Wages',wg)

        
