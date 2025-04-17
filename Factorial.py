def factorial(n):
    ans=1
    for i in range(1,n+1):
        ans *=i
    return ans
    
num=int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")