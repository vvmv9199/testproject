no=input("enter your name")
nm=input("enter name of item");
pr=int(input("enter price per item"))
qty=int(input("Enter quantity purchased"))
bill=int(input("enter total amount"))
dis=(10/100)*pr;
net=pr-dis;
print("item number:",no)
print("item name:",nm)
print("price of item:",pr);
print("quantity purchaed:",qty);
print("bill:",bill)
print("discount:",dis)
print("net bill:",net)
