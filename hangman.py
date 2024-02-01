import random

def choose_word():
    file_path = "C:/Users/ashri/Downloads/Myprojects_/hangman/words.txt"  
    with open(file_path, "r") as file:
        words = file.readlines()
    return random.choice(words).strip()
    

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    print("Welcome to Hangman!")
    word_to_guess = choose_word().lower()
    guessed_letters = []
    incorrect_attempts = 0
    max_attempts = 6

    while True:
        current_display = display_word(word_to_guess, guessed_letters)
        print("Current word: ", current_display)

        if current_display == word_to_guess:
            print("Congratulations! You guessed the word:", word_to_guess)
            break

        guess = input("Guess a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in word_to_guess:
                guessed_letters.append(guess)
                print("Good guess!")
            else:
                incorrect_attempts += 1
                print("Incorrect guess. Attempts left:", max_attempts - incorrect_attempts)

                if incorrect_attempts == max_attempts:
                    print("Sorry, you ran out of attempts. The correct word was:", word_to_guess)
                    break
        else:
            print("Invalid input. Please enter a single letter.")

if __name__ == "__main__":
    hangman()
