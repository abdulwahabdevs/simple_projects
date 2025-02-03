import itertools
import string
import time

def common_guess(word: str) -> str | None:
    with open('words.txt') as file:
        guesses: str = file.read().splitlines()
        for i, guess in enumerate(guesses, start=1):
            if word == guess:
                return f'"Common word: {guess} (#{i})"'


def brute_force(word: str, length: int, symbols: bool=False, digits: bool=False):
    chars: str = string.ascii_lowercase

    # we check it includes symbols
    if symbols:
        chars += string.punctuation
    # we check it includes digits
    if digits:
        chars += string.digits

    attempts: int = 0
    for guess in itertools.product(chars, repeat=length):
        attempts += 1
        guess: str = ''.join(guess)

        if guess == word:
            print(f'"{word} was cracked in {attempts:,} attempts"')

def main():
    print("Searching...")
    password: str = 'abc1'

    start_time: float = time.perf_counter()
    if common_match := common_guess(password):
        return common_match
    else:
        if cracked := brute_force(password, len(password), symbols=False, digits=True ):
            return cracked
        else:
            print("There was not match")

    end_time: float = time.perf_counter()
    print(f"Time: {round(end_time - start_time, 2)} seconds")

if __name__ == '__main__':
    main()

