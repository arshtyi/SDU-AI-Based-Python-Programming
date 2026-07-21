def last_digit(num):
    """
    Return the final decimal digit of a positive integer.

    :param num: (int) a positive integer
    :return: (int) the final digit of num
    """
    return num % 10


def decimal_right_shift(num):
    """
    Remove the final decimal digit from an integer.

    :param num: (int) a positive integer
    :return: (int) num with its final digit removed
    """
    return num // 10


def sum_digits(num3):
    """
    Return the sum of the digits in a positive three-digit integer.

    :param num3: (int) a positive three-digit integer
    :return: (int) the sum of the three digits in num3
    """
    ones_digit = last_digit(num3)
    remaining_digits = decimal_right_shift(num3)
    tens_digit = last_digit(remaining_digits)
    hundreds_digit = decimal_right_shift(remaining_digits)

    return hundreds_digit + tens_digit + ones_digit


def main():
    """
    Ask for a three-digit positive integer and print its digit sum.

    :return: (None) this function displays the result to the user
    """
    number = int(input("Please enter a 3-digit positive integer:\n"))

    # Keep asking until the integer is within the three-digit range. This also
    # rejects inputs such as 000 because int("000") has the value zero.
    while number < 100 or number > 999:
        number = int(input("Please enter a 3-digit positive integer:\n"))

    digit_sum = sum_digits(number)
    print(f"The sum of the digits of {number} is {digit_sum}")


if __name__ == "__main__":
    main()
