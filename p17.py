no=int(input("Enter item no"))
nm=input("Enter name of the item")
pr=float(input("Enter price per item"))
qty=int(input("Enter quantity"))
tot=pr*qty
print(tot)
if(tot>=5000):
    net=tot*(10/100)
else:
    net=tot*(8/100)
print(net)
receipt=tot-net
print(receipt)
        
