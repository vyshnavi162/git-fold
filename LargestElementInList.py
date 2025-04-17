def largest_element(lst):
    return max(lst)

n = int(input("How many elements do you want to enter? "))
numbers = []

for i in range(n):
    num = int(input("Enter a number: "))
    numbers.append(num)

print(f"List is: {numbers}")
print(f"Largest element in the list is {largest_element(numbers)}")
