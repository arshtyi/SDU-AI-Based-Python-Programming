password_is_valid = False

while not password_is_valid:
    password = input("Please enter your password:\n")

    lowercase_count = 0
    uppercase_count = 0
    number_count = 0
    special_character_count = 0

    for character in password:
        if "a" <= character <= "z":
            lowercase_count += 1
        elif "A" <= character <= "Z":
            uppercase_count += 1
        elif "0" <= character <= "9":
            number_count += 1
        elif character in "!@#$":
            special_character_count += 1

    if len(password) < 8:
        print("Password should contain at least 8 characters")
    elif lowercase_count < 2:
        print("Password should contain at least 2 lowercase letters")
    elif uppercase_count < 1:
        print("Password should contain at least 1 uppercase letter")
    elif number_count < 2:
        print("Password should contain at least 2 numbers")
    elif special_character_count < 1:
        print("Password should contain at least 1 of the characters !@#$")
    else:
        password_is_valid = True
        print(f"Password {password} is a valid password")
