n=int(input("Enter a positive Number: "))
sum=0

for i in range(n):
    if(n%2==0):
        sum +=i
    else:
        print(n, "is a Odd Number")
print(f"Sum of first {n} even numbers: ", sum)