# Starter Code for Hangman Game Assignment

import random

# List of possible words
words = ['python', 'hangman', 'challenge', 'programming', 'computer']


def play_hangman(word_list=words, max_incorrect=6, guesser=input, on_progress=print):
    # Randomly select a word from the list
    secret_word = random.choice(word_list)

    # Initialize variables for game state
    guessed_letters = set()
    incorrect_guesses = 0

    # Main game loop
    while incorrect_guesses < max_incorrect and set(secret_word) - guessed_letters:
        progress = " ".join(letter if letter in guessed_letters else "_" for letter in secret_word)
        on_progress(f"Word: {progress}  |  Incorrect guesses: {incorrect_guesses}/{max_incorrect}")

        guess = guesser("Guess a letter: ").strip().lower()

        if not guess or len(guess) != 1 or not guess.isalpha():
            on_progress("Please guess a single letter.")
            continue

        if guess in guessed_letters:
            on_progress(f"You already guessed '{guess}'.")
            continue

        guessed_letters.add(guess)

        if guess not in secret_word:
            incorrect_guesses += 1

    won = not (set(secret_word) - guessed_letters)

    # Print win/lose message
    if won:
        on_progress(f"You win! The word was '{secret_word}'.")
    else:
        on_progress(f"You lose! The word was '{secret_word}'.")

    return won


if __name__ == "__main__":
    play_hangman()
