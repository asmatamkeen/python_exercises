import random
import sys
import logo_art

numbers=list(range(1,101))

print(logo_art.logo)

print("Let me think of a number between 1 to 100")
number= random.choice(numbers)
level=input("Choose level of difficulty. Type 'easy or 'hard':")
if level == 'easy':
    guesses=10
elif level == 'hard':
    guesses=5
else:
    print("Invalid input.")
    sys.exit(0)

print(f"You have {guesses} attempts to guess the number")
while guesses > 0:
    guessed_number = int(input("Make a guess:"))
    if guessed_number == number:
        print(f"Your guess is right. The answer was {number}")
        sys.exit(0)
    elif guessed_number < number:
        print("Your Guess is Too Low")
    else:
        print("Your Guess is Too High")
    
    
    guesses = guesses - 1
    if guesses > 0:
        print(f"Guess again. You have {guesses} attempts remaining to guess the number.")

print("You are out of guesses. You Lose")
