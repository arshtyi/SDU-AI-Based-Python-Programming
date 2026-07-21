# NOTE: This file MUST be named test_SOMETHING, i.e. not SOMETHING_test
# And the functions in it must start with test_SOMETHING not SOMETHING_test
# if you want them to be run as tests (via auto-discovery)

import unittest
from gradescope_utils.autograder_utils.decorators import weight, visibility

from creditcard import *
from creditcard_part1 import *

def autograder_last_digit(num):
    """
    Computes the last digit of the num

    :param num: (int) a positive integer
    :return: (int) the last digit of num
    """
    return num % 10


def autograder_decimal_right_shift(num):
    """
    Right shifts num by one digit
    
    :param num: (int) a positive intger
    :return: (int) num right shifted by one digit
    """
    return num // 10


def autograder_luhn_sum(number):
    """
    Generate the last digit of the 13-digit credit card number by following the Luhn's algorithm.

    :param num: (int) a generated 12-digit number
    :return: (int) the last digit that makes the 13-digit
            number a valid credit card number
    """
    sum = 0
    for i in range(13):
        digit = autograder_last_digit(number)
        if i % 2 == 0:
            # simply add the even position digits
            sum += digit
        else:
            # double the odd position digits
            if digit < 5:
                sum += 2 * digit
            else:
                sum += (2 * digit) - 9
        number = autograder_decimal_right_shift(number)

    return sum


def autograder_verify(number13):
    """
    check verify function using autograder luhn sum
    """
    return autograder_luhn_sum(number13) % 10 == 0


def check_luhn_sum(number):
    if luhn_sum(number) == autograder_luhn_sum(number):
        return True
    else:
        print("luhn_sum failed")
        print("Input to the function: '" + str(number) + "'")
        print("Expected return value: '" + str(autograder_luhn_sum(number)) + "'")
        print("Received return value: '" + str(luhn_sum(number)) + "'")
        return False


def check_verify(number):
    if verify(number) == autograder_verify(number):
        return True
    else:
        print("verify failed")
        print("Input to the function: '" + str(number) + "'")
        print("Expected return value: '" + str(autograder_verify(number)) + "'")
        print("Received return value: '" + str(verify(number)) + "'")
        return False


def check_generate(number):
    creditcard_number = generate(number)
    if autograder_verify(creditcard_number):
        return True
    else:
        print("generate failed")
        print("Input to the function: '" + str(number) + "'")
        print("Received return value: '" + str(creditcard_number) + "'")
        print("Feedback: " + str(creditcard_number) + " is not a valid creditcard number.")
        return False


class Autograder(unittest.TestCase):
    @weight(1)
    def test_verify_1(self):
        self.assertEqual(check_verify(9813428854407), True)

    @weight(1)
    @visibility('after_due_date')
    def test_verify_2(self):
        self.assertEqual(check_verify(1111111111112), True)

    @weight(1)
    @visibility('after_due_date')
    def test_verify_3(self):
        self.assertEqual(check_verify(2020202020208), True)

    @weight(1)
    @visibility('after_due_date')
    def test_verify_4(self):
        self.assertEqual(check_verify(9999999999992), True)

    @weight(1)
    @visibility('after_due_date')
    def test_verify_5(self):
        self.assertEqual(check_verify(1234561447355), True)

    @weight(2)
    def test_luhn_sum_1(self):
        self.assertEqual(check_luhn_sum(9999929999997), True)

    @weight(2)
    @visibility('after_due_date')
    def test_luhn_sum_2(self):
        self.assertEqual(check_luhn_sum(1111111111110), True)

    @weight(2)
    @visibility('after_due_date')
    def test_luhn_sum_3(self):
        self.assertEqual(check_luhn_sum(1000000000001), True)

    @weight(2)
    @visibility('after_due_date')
    def test_luhn_sum_4(self):
        self.assertEqual(check_luhn_sum(5555555555555), True)

    @weight(2)
    @visibility('after_due_date')
    def test_luhn_sum_5(self):
        self.assertEqual(check_luhn_sum(1056753150955), True)

    @weight(2)
    def test_generate_1(self):
        self.assertEqual(check_generate(123456), True)

    @weight(2)
    @visibility('after_due_date')
    def test_generate_2(self):
        self.assertEqual(check_generate(111110), True)

    @weight(2)
    @visibility('after_due_date')
    def test_generate_3(self):
        self.assertEqual(check_generate(105675), True)

    @weight(2)
    @visibility('after_due_date')
    def test_generate_4(self):
        self.assertEqual(check_generate(100000), True)

    @weight(2)
    @visibility('after_due_date')
    def test_generate_5(self):
        self.assertEqual(check_generate(999999), True)



