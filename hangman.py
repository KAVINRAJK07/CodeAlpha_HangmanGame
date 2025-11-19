import random

def hangman():
    words = ["python", "laptop", "program", "coffee", "mobile"]
    chosen_word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("🎮 Welcome to Hangman Game!")
    print("_ " * len(chosen_word))

    while attempts > 0:
        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess not in chosen_word:
            attempts -= 1
            print(f"Wrong guess! Attempts left: {attempts}")
        else:
            print("Correct guess!")

        # Display current progress
        display = ""
        for letter in chosen_word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "

        print(display)

        # Check if player won
        if "_" not in display:
            print("🎉 Congratulations! You guessed the word:", chosen_word)
            break

    else:
        print("❌ You lost! The word was:", chosen_word)

hangman()
