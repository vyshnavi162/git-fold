def sequence(n):
    a,b= 0, 1
    fib=[ ]

    for i in range(n):
        fib.append(a)
        a,b = b, a+b
        
    return fib

a=int(input("Enter a number: "))
print(sequence(a))