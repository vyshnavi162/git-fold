a=int(input("Enter first no.: "))
b=int(input("Enter second no.: "))
c=int(input("Enter third no.: "))
if(a>b & a>c):
    print(a," is the largest number")
elif(b>a & b<c):
    print(b," is the largest number")
else:
    print(c," is the largest number")
