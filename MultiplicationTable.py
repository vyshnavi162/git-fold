def table(n,till=10):
    for i in range(1,11):
        print(f"{n} x {i} = {n * i}")

num = int(input("Enter a number: "))
print(f"Multiplication table for {num}:\n")
table(num)
