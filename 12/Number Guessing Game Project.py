import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
choose_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

def rand_num_generator():
    return random.randint(1,100)

generated_number = rand_num_generator()
def too_high(user_guess):
    if user_guess > generated_number:
        print("Too high.")
        print("Guess again.")
def too_low(user_guess):
    if user_guess < generated_number:
        print("Too low.")
        print("Guess again")

if choose_difficulty == "easy":
    lives = 10
    print(f"You have {lives} attempts to guess the number.")
else:
    lives = 5
    print(f"You have {lives} attempts to guess the number.")

rand_num_generator()
while lives > 0:
    user_guess = int(input("Make a guess: "))

    too_low(user_guess)
    too_high(user_guess)

    if user_guess != generated_number:
        lives -= 1
        print(f"You have {lives} attempts remaining to guess the number.")
        if lives == 0:
            print(f"Sorry, you ran out of lives, the random number was: {generated_number} ")
    else:
        print(f"You got it! The answer was {generated_number}")
        break
