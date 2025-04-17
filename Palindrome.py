print("PALINDROME CHECKER")

# PALINDROME PROGRAM F0R STRING
def palindrome(s):
    s=s.replace(" "," ").lower()
    return s== s[::-1]

text=input("Enter a string: ")

if palindrome(text):
    print(f"{text} is palindrome.")
else:
    print(f"{text} is not palindrome.")



# PALINDROME PROGRAM F0R NUMBER
def is_palindrome_number(n):
    return str(n) == str(n)[::-1]

num = int(input("Enter a number: "))

if is_palindrome_number(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")