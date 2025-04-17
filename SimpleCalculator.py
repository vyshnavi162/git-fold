print("SIMPLE CALCULATOR (+,-,*,/,%,**)")

def add(a, b):
    print(a + b)

def sub(a, b):
    print(a - b)

def mul(a, b):
    print(a * b)

def div(a, b):
    if b != 0:
        print(a / b)
    else:
        print("Error: Division by zero")

def rem(a, b):
    if b != 0:
        print(a % b)
    else:
        print("Error: Division by zero")

def pow(a, b):
    print(a ** b)

a = int(input("Enter first Number: "))
b = int(input("Enter second Number: "))

print("SUM:", end=" ")
add(a, b)

print("DIFFERENCE:", end=" ")
sub(a, b)

print("MULTIPLICATION:", end=" ")
mul(a, b)

print("DIVISION:", end=" ")
div(a, b)

print("REMAINDER: ",end=" ")
rem(a, b)

print(f"EXPONENT: ",end=" ")
pow(a, b)

