from random import randint

from creditcard_part1 import decimal_right_shift, last_digit


def luhn_sum(number13):
    """
    Compute the Luhn sum of a 13-digit integer.

    Starting at the rightmost check digit, every second digit is doubled. If
    a doubled digit has two digits, those two digits are added together.

    :param number13: (int) a 13-digit credit card number
    :return: (int) the Luhn sum of number13
    """
    remaining_number = number13
    total = 0

    # Work from right to left so that positions alternate naturally, beginning
    # with the unaffected check digit at position zero.
    for position in range(13):
        digit = last_digit(remaining_number)

        if position % 2 == 0:
            total += digit
        else:
            doubled_digit = digit * 2

            # A doubled decimal digit is at most 18, so its digit sum is the
            # ones digit plus the remaining tens digit.
            total += last_digit(doubled_digit)
            total += decimal_right_shift(doubled_digit)

        remaining_number = decimal_right_shift(remaining_number)

    return total


def verify(number13):
    """
    Determine whether a 13-digit integer passes the Luhn algorithm.

    :param number13: (int) a 13-digit credit card number
    :return: (bool) True when number13 passes Luhn verification; otherwise False
    """
    return last_digit(luhn_sum(number13)) == 0


def generate(number6):
    """
    Generate a valid 13-digit card number beginning with six given digits.

    :param number6: (int) a six-digit prefix
    :return: (int) a valid 13-digit number beginning with number6
    """
    number12 = number6

    # Append six independently generated digits. Each position can contain
    # every digit from zero through nine, including leading zeroes in this part.
    for unused_position in range(6):
        number12 = number12 * 10 + randint(0, 9)

    # Reserve the final position for the check digit. If zero is not already a
    # valid check digit, the missing amount to the next multiple of ten is.
    number13 = number12 * 10
    if not verify(number13):
        number13 += 10 - last_digit(luhn_sum(number13))

    return number13


def main():
    """
    Ask for a six-digit prefix and print three valid card numbers using it.

    :return: (None) this function displays the generated numbers to the user
    """
    number6 = int(input("Enter a 6 digit number:\n"))

    while number6 < 100000 or number6 > 999999:
        number6 = int(input("Enter a 6 digit number:\n"))

    print("\nThree valid numbers:")
    for unused_number in range(3):
        print(generate(number6))


if __name__ == "__main__":
    main()
