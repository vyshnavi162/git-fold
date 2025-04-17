def binary_to_decimal(binary_str):
    return int(binary_str, 2)

binary_input = input("Enter a binary number: ")
decimal_output = binary_to_decimal(binary_input)

print(f"The decimal equivalent of binary {binary_input} is: {decimal_output}")