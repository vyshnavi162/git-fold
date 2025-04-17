


def digits(n):
    count = 0
    for i in str(n):
        count += int(i)  
    
    return count

num = int(input("Enter a number: "))
print(f"Sum of digits: {digits(num)}")
