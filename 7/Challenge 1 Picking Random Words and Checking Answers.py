#Step 1

import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.


# generated_word = random.randint(0, len(word_list) - 1)

chosen_word = random.choice(word_list)

number_of_lives = 7
letters = []
for letter in chosen_word:
    letters += list(letter)
print(letters)

while number_of_lives > 0:
    guess = input("Guess a letter: ").lower()
    if guess in letters:
        print("Correct guess")
    else:
        print("Wrong guess")
        number_of_lives -= 1


