from random import choice

def run_hangman():
    # could've done better with more words in a random list rather than this
    word: str = choice(['counter', 'strike', 'shawarma', 'accelerate', 'batman'])

    # greeting user
    username: str = input("Please enter your username: ")
    print(f"Welcome hangman game, {username}!")

    # set up
    guessed: str = ''
    tries: int = 3

    while tries > 0:
        blanks: int = 0

        print('Word: ', end='')
        for char in word:
            if char in guessed:
                print(char, end=' ')
            else:
                print('_', end=' ')
                blanks += 1

        print()    # to add a blank line
        if blanks == 0:
            print("You, guessed the word!")
            break

        # getting the guess
        guess: str = input('Guess a letter: ')

        # in order to avoid multiple guess entries in one go
        # check if the word is correctly guessed or len > 1 no more than one letter
        if guess.lower() != word and len(guess) > 1:
            print("Too many guesses, enter a letter again.")
            continue

        # if already guessed give more chance to user
        if guess.lower() in guessed:
            print(f'You already guessed the letter "{guess}"! Please guess again.')
            continue

        guessed += guess.lower()

        if guess.lower() not in word:
            tries -= 1
            print(f"Wrong guess, tries left: {tries}!")
            if tries == 0:
                print("Game over!")


if __name__ == '__main__':
    run_hangman()
