import random

def roll_dice(amount: int = 2) -> list:
    if amount <= 0:
        raise ValueError("Amount must be greater than 0")

    rolls: list[int] = []
    for i in range (amount):
        rolls.append(random.randint(1, 6))
    return rolls

def main():
    while True:
        try:
            user_input: str = input('How many dice would you like to roll? ')

            if user_input.lower() == 'exit':
                print('Thanks for playing!')
                break
            numbers: list[int] = roll_dice(int(user_input))
            print(*numbers, sep=',')
            print(f"Sum: {sum(numbers)}", end='\n')
        except ValueError:
            print('Please enter a valid input or exit to quit!')
            continue


if __name__ == '__main__':
    main()