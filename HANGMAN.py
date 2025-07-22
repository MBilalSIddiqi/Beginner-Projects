import random

# List of words
words = ["hi", "bye"]

# Selecting a word
chosen_word = random.choice(words)

# Display list with underscores
display = ['_' for _ in chosen_word]
print(' '.join(display))

# Number of wrong guesses allowed
attempts = 5

while True:
    guess = input("\nEnter a letter: ").lower()
    correct_guess = False

    for index, letter in enumerate(chosen_word):
        if letter == guess:
            display[index] = letter
            correct_guess = True

    if not correct_guess:
        attempts -= 1
        print(f"Wrong guess! Lives left: {attempts}")

    print(' '.join(display))

    # Win condition
    if "_" not in display:
        print("Congratulations! You guessed the word!")
        break

    # Lose condition
    if attempts == 0:
        print(f"Game over! The word was: {chosen_word}")
        break