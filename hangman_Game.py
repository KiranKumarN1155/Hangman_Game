import random

def choose_word():
    """Selects a random word from a list."""
    words = ["python", "java", "javascript", "kotlin", "swift", "ruby", "csharp", "go", "typescript", "php"]
    return random.choice(words).upper()

def display_word(word, guessed_letters):
    """Displays the word with correctly guessed letters and underscores for unguessed letters."""
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()

def hangman():
    """Plays a game of Hangman."""
    word_to_guess = choose_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_guesses = 6  # You can adjust the number of allowed incorrect guesses

    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))

    while "_" in display_word(word_to_guess, guessed_letters) and incorrect_guesses < max_guesses:
        guess = input("Guess a letter: ").upper()

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Correct guess!")
            print(display_word(word_to_guess, guessed_letters))
        else:
            incorrect_guesses += 1
            print(f"Incorrect guess. You have {max_guesses - incorrect_guesses} guesses left.")
            print(display_word(word_to_guess, guessed_letters))

            # Basic hangman visual (you can make this more elaborate)
            if incorrect_guesses == 1:
                print("   O   ")
            elif incorrect_guesses == 2:
                print("   O   ")
                print(r"   |   ")
            elif incorrect_guesses == 3:
                print("   O   ")
                print(r"  /|   ")
            elif incorrect_guesses == 4:
                print("   O   ")
                print(r"  /|\  ")
            elif incorrect_guesses == 5:
                print("   O   ")
                print(r"  /|\  ")
                print(r"  /    ")
            elif incorrect_guesses == 6:
                print("   O   ")
                print(r"  /|\  ")
                print(r"  / \  ")



    if "_" not in display_word(word_to_guess, guessed_letters):
        print(f"Congratulations! You guessed the word: {word_to_guess}")
    else:
        print(f"You ran out of guesses. The word was: {word_to_guess}")

if __name__ == "__main__":
    hangman()