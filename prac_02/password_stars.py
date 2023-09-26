""""""
MINIMUM_LENGTH = 6


def main():
    password = input("Password: ")
    determine_valid_password(password, MINIMUM_LENGTH)
    print_asterisks(password)


def determine_valid_password(password, MINIMUM_LENGTH):
    while len(password) < MINIMUM_LENGTH:
        print("Invalid Password")
        password = input("Password: ")
    return password


def print_asterisks(password):
    print("*" * (len(password)))


main()
