"""
CS51P - Password Validation

This module checks and validates the password entered by the users.
The basic requirements are as follows:
    1. Minimum length of transaction password is 8
    3. At least 2 lowercase letters
    4. At least 1 uppercase letter 
    5. At least 2 numbers
    6. At least 1 character from [!@#$]

Author: Eleanor Birrell
"""

valid = False

while not valid:
    password = input("Please enter your password:\n")

    char_count = 0
    lower_count = 0
    upper_count = 0
    digit_count = 0
    special_count = 0

    for c in password:
        if c >= 'a' and c <= 'z':
            lower_count += 1
        elif c >= 'A' and c <= 'Z':
            upper_count += 1
        elif str.isdigit(c):
            digit_count += 1
        elif c == '!' or c == '@' or c == '#' or c == '$':
            special_count += 1
        
        char_count += 1

    if char_count < 8:
        print("Password should contain at least 8 characters")
    elif lower_count < 2:
        print("Password should contain at least 2 lowercase letter")
    elif upper_count < 1:
        print("Password should contain at least 1 uppercase letter")
    elif digit_count < 2:
        print("Password should contain at least 2 numbers")
    elif special_count == 0:
        print("Password should contain at least 1 of the characters !@#$")
    else:
        valid = True

print("Password " + password + " is a valid password")


