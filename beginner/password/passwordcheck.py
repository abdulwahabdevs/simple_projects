def check_password(password: str):
    with open('passwords.txt', 'r') as file:
        common_passwords = file.read().splitlines()

    for i, common_password in enumerate(common_passwords, start=1):
        if password == common_password:
            print(f"{password}: ⛔️(#{i}) common pasword")
            return
        if password == '' or len(password) == 1:
            print(f"Please restart and enter valid password.")
            return

    print(f"{password}: ✅Unique")


def main():
    user_input: str = input("Enter the password to check: ")
    check_password(user_input)

if __name__ == '__main__':
    main()
