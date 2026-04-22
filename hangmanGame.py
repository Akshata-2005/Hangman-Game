import random

# Predefined list of words
words = ["python", "apple", "banana", "orange", "grapes"]

# Choose a random word
secret_word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")

# Game loop
while incorrect_guesses < max_guesses:
    # Display current progress
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word.strip())
    print(f"Incorrect guesses left: {max_guesses - incorrect_guesses}")

    # Check if player has won
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word!")
        break

    # Get user input
    guess = input("Enter a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        incorrect_guesses += 1
    print("❌ Invalid input! Only one letter is allowed.")
    print(f"Incorrect guesses left: {max_guesses - incorrect_guesses}")
    continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess not in secret_word:
        incorrect_guesses += 1
        print("❌ Wrong guess!")

# Loss condition
if incorrect_guesses == max_guesses:
    print("\n💀 Game Over!")
    print(f"The word was: {secret_word}")
