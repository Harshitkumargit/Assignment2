l1=input("Enter length of one side ")
l2=input("Enter length of second side ")
l3=input("Enter length of third side ")

l1=int(l1)
l2=int(l2)
l3=int(l3)

if l1+l2<l3 or l2+l3<l1 or l1+l3<l2:
    print("No")
else:
    print("Yes")
