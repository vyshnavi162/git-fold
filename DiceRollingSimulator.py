import random

def roll_dice():
    return random.randint(1, 6)

total_sum = 0
six_count = 0  # Counter for consecutive sixes

while True:
    user_input = input("Type 'roll' to roll the dice or 'exit' to quit: ").lower()
    if user_input == 'roll':
        roll = roll_dice()
        print(f"You rolled a {roll}!")
        total_sum += roll
        
        if roll == 6:
            six_count += 1
            if six_count == 3:
                print("6 rolled thrice. Goodbye!")
                break
            print("You get another chance to roll!")
        else:
            six_count = 0  # Reset six counter if roll is not a 6
    elif user_input == 'exit':
        print(f"Goodbye! The total sum of your rolls is {total_sum}.")
        break
    else:
        print("Invalid input. Please type 'roll' or 'exit'.")