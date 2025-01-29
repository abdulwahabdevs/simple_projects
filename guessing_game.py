from random import randint

lower_num, higher_num = 1, 10
random_number = randint(lower_num, higher_num)
print(f'Guess a number between {lower_num} and {higher_num}.')

attempts = 2
while True:
    try:
        user_guess: int = int(input('Guess a number: '))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if user_guess < random_number and attempts > 0:
        print(f"Too low, try again. {attempts} attempts left.")
        attempts -= 1
        continue
    if user_guess > random_number and attempts > 0:
        print(f"Too high, try again. {attempts} attempts left.")
        attempts -= 1
        continue
    if user_guess == random_number:
        print(f'You guessed {user_guess} right!.')
        break
    else:
        print(f'You are out of attempts. Start again.')
        break