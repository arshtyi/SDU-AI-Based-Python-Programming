"""
    CS051P Lab Assignments: Credit Cards

    Author: YOUR-NAME-HERE

    Date:   WHEN YOU COMPLETED IT

    The goal of this assignment is to give you more practice with functions,
    including testing functions.
"""
from random import randint
from creditcard_part1 import last_digit, decimal_right_shift, sum_digits


def luhn_sum(number):
    """
    Generate the last digit of the 13-digit credit card number by following the Luhn's algorithm.

    :param num: (int) a generated 12-digit number
    :return: (int) the last digit that makes the 13-digit
            number a valid credit card number
    """
    sum = 0
    for i in range(13):
        digit = last_digit(number)
        if i % 2 == 0:
            # simply add the even position digits
            sum += digit
        else:
            # double the odd position digits
            if digit < 5:
                sum += 2 * digit
            else:
                sum += (2 * digit) - 9
        number = decimal_right_shift(number)

    return sum


def verify(number):
    """
    Verify if the number is a valid credit card number according to Luhn's algorithm

    :param number13: (int) a generated 13-digit number
    :return: True or False
    """
    return last_digit(luhn_sum(number)) == 0


def generate(number6):
    """
    Generate a 13-digit number that is a valid credit card number following the Luhn's algorithm.

    :param number6: (int) the input 6-digit number
    :return: (int) a 13-digit valid credit card number
    """
    # Step 1: generate 12 digit number
    twelve_digit = number6 * 1000000
    twelve_digit += randint(0, 999999)

    # Step 2: generate a 13 digit number
    thirteen_digit = twelve_digit * 10

    # Step 3: generate the valid 13-digit number by adding checksum
    if not verify(thirteen_digit):
        thirteen_digit += 10 - last_digit(luhn_sum(thirteen_digit))

    return thirteen_digit


def main():
    """
    Ask for a 6-digit input from user and generate a 13-digit number that
    starts with the given 6-digit and is a valid credit card number
    verified by Luhn's algorithm
    """
    six_digit = int(input("Please enter a 6 digit number: \n"))
    
    print("Three valid credit card numbers are:")
    
    for times in range(3):
        thirteen_digit = generate(six_digit)
        if verify(thirteen_digit):
            print(thirteen_digit)

    # print(luhn_sum(1056758686720))
    # print(verify(1056758686721))





if __name__ == "__main__":
    main()
