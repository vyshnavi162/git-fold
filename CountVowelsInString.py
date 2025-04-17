def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    
    for i in s:  # Iterate over each character in the string
        if i in vowels:  # Check if the character is a vowel
            count += 1  
    
    return count

input_string = input("Enter a string: ")
print(f"Number of vowels in the string: {count_vowels(input_string)}")
