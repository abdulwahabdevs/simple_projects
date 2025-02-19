import string
import secrets


def contains_upper(password: str)-> bool:
    for char in password:
        if char.upper():
            return True
    return False

def contains_symbol(password: str)-> bool:
    for char in password:
        if char in string.punctuation:
            return True
    return False

def password_generator(length: int, symbol: bool, uppercase: bool):
    combination: str = string.ascii_lowercase + string.digits
    if symbol:
        combination += string.punctuation
    if uppercase:
        combination += string.ascii_uppercase

    combination_length: int = len(combination)
    new_password: str = ''
    for _ in range(length):
        new_password += combination[secrets.randbelow(combination_length)]

    return new_password

if __name__ == '__main__':
    print("Welcome to Password Generator!")
    length_input = int(input("Length of password: "))
    symbol_input = bool(int(input("Symbol? (Yes-> 1 / No -> 0): ")))
    uppercase_input = bool(int(input("Uppercase? (Yes-> 1 / No -> 0): ")))
    for i in range(1, 6):
        new: str = password_generator(length= length_input, symbol= symbol_input, uppercase= uppercase_input)
        specs: str = f'U: {contains_upper(new)}, S: {contains_symbol(new)}, L: {len(new)}'
        print(f'{i} -> {new} | {specs}')
