MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = get_password()
    while not is_valid_password(password):
        print("Invalid password!")
        password = get_password()
    print("Your {}-character password is valid: {}".format(len(password),password))

def get_password():
    import getpass
    return (getpass.getpass("> "))

def is_valid_password(password):

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if char.isdigit():
            count_digit = count_digit + 1
        elif char.islower():
            count_lower = count_lower + 1
        elif char.isupper():
            count_upper = count_upper + 1
        elif char in SPECIAL_CHARACTERS:
            count_special = count_special + 1

    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False
    elif count_digit == 0 or count_lower == 0 or count_upper == 0:
        return False
    elif SPECIAL_CHARS_REQUIRED is True and count_special == 0:
        return False
    else:
        return True

main()