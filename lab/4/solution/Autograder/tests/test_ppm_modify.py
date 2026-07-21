# NOTE: This file MUST be named test_SOMETHING, i.e. not SOMETHING_test
# And the functions in it must start with test_SOMETHING not SOMETHING_test
# if you want them to be run as tests (via auto-discovery)

import unittest
from gradescope_utils.autograder_utils.decorators import weight, visibility

from ppm_modify import *
import math


def autograder_negate(line):
    """
    turn each numeric valure into its complement mod 255
    :param (str) line: numbers to be negated
    :return (str): line containing the negated numbers
    """
    # pull apart the fields
    numbers = line.strip().split()

    # assemble a string of negations
    result = ""
    for value in numbers:
        negative = 255 - int(value)
        if result is "":
            result = str(negative)
        else:
            result += " " + str(negative)

    return result


def autograder_grey_scale(line):
    """
    replace each of the three per-pixel color values with corresponding grey
    :param (str) line: numbers to be grey-scaled
    :return (str): line containing the grey-scaled numbers
    """
    # pull apart the fields
    numbers = line.strip().split()

    # assemble a string of negations
    result = ""

    for i in range(0, len(numbers), 3):
        # read colors and compute the grey value
        r = int(numbers[i])
        g = int(numbers[i+1])
        b = int(numbers[i+2])
        grey = int(math.sqrt(r**2 + g**2 + b**2))
        if grey > 255:
            grey = 255

        # append the new 3 values to the line
        if result != "":
            result += " "
        result += str(grey) + " " + str(grey) + " " + str(grey)

    return result


def autograder_remove_color(line, color):
    """
    remove the specified color from every pixel
    :param (str) line: numbers to have color remvoed
    :return (str): line containing same pixels, less selected color
    """
    # pull apart the fields
    numbers = line.strip().split()

    # assemble a string of negations
    result = ""

    for i in range(0, len(numbers), 3):
        # read colors and execept for the one to remove
        r = 0 if color == "red" else int(numbers[i])
        g = 0 if color == "green" else int(numbers[i+1])
        b = 0 if color == "blue" else int(numbers[i+2])

        # append these three colors to the output line
        if result != "":
            result += " "
        result += str(r) + " " + str(g) + " " + str(b)

    return result


def check_negate(line):
    if negate(line).strip().split() == autograder_negate(line).strip().split():
        return True
    else:
        print("negate failed")
        print("Input to the function: '" + line + "'")
        print("Expected return value: " + autograder_negate(line))
        print("Received return value: " + negate(line))
        return False


def check_grey_scale(line):
    if grey_scale(line).strip().split() == autograder_grey_scale(line).strip().split():
        return True
    else:
        print("grey_scale failed")
        print("Input to the function: '" + line + "'")
        print("Expected return value: " + autograder_grey_scale(line))
        print("Received return value: " + grey_scale(line))
        return False


def check_remove_color(line, color):
    if remove_color(line, color).strip().split() == autograder_remove_color(line, color).strip().split():
        return True
    else:
        print("grey_scale failed")
        print("Input to the function: line='" + line + "', color='" + color + "'")
        print("Expected return value: " + autograder_remove_color(line, color))
        print("Received return value: " + remove_color(line, color))
        return False


class Autograder(unittest.TestCase):
    # test negate
    @weight(1)
    def test_negate_1(self):
        self.assertEqual(check_negate("10 20 30"), True)

    @weight(1)
    @visibility('after_due_date')
    def test_negate_2(self):
        self.assertEqual(check_negate("10 20 30 40 50 60"), True)

    @weight(1)
    @visibility('after_due_date')
    def test_negate_3(self):
        self.assertEqual(check_negate("255 255 255"), True)

    @weight(1)
    @visibility('after_due_date')
    def test_negate_4(self):
        self.assertEqual(check_negate("0 0 0"), True)

    @weight(1)
    @visibility('after_due_date')
    def test_negate_5(self):
        self.assertEqual(check_negate("10\t20\t30\t40\t50\t60"), True)

    @weight(1)
    @visibility('after_due_date')
    def test_negate_6(self):
        self.assertEqual(check_negate(""), True)

    @weight(1)
    @visibility('after_due_date')
    def test_negate_7(self):
        self.assertEqual(check_negate("100 203 23 7 19 23 67 68 69 100 123 23"), True)

    @weight(1)
    @visibility('after_due_date')
    def test_negate_8(self):
        self.assertEqual(check_negate("47   47   47   48   48   48   49   49   49  "), True)



    # test grey_scale
    @weight(1)
    def test_grey_scale_1(self):
        self.assertEqual(check_grey_scale("10 20 30"), True)

    @weight(1)
    @visibility('after_due_date')
    def test_grey_scale_2(self):
        self.assertEqual(check_grey_scale("10 20 30 40 50 60"), True)

    @weight(1)
    @visibility('after_due_date')
    def test_grey_scale_4(self):
        self.assertEqual(check_grey_scale("255 255 255"), True)

    @weight(1)
    @visibility('after_due_date')
    def test_grey_scale_5(self):
        self.assertEqual(check_grey_scale("10 20 30 200 200 200"), True)

    @weight(1)
    @visibility('after_due_date')
    def test_grey_scale_3(self):
        self.assertEqual(check_grey_scale("0 0 0"), True)

    @weight(1)
    @visibility('after_due_date')
    def test_grey_scale_6(self):
        self.assertEqual(check_grey_scale(""), True)

    @weight(1)
    @visibility('after_due_date')
    def test_grey_scale_7(self):
        self.assertEqual(check_grey_scale("2\t7\t26"), True)

    @weight(1)
    @visibility('after_due_date')
    def test_grey_scale_8(self):
        self.assertEqual(check_grey_scale("50 100 100 50 100 100 50 100 100"), True)

    
     
    # test remove_color
    @weight(1)
    def test_remove_color_1(self):
        self.assertEqual(check_remove_color("10 20 30", "red"), True)

    @weight(1)
    @visibility('after_due_date')
    def test_remove_color_2(self):
        self.assertEqual(check_remove_color("10 20 30 40 50 60", "green"), True)

    @weight(1)
    @visibility('after_due_date')
    def test_remove_color_3(self):
        self.assertEqual(check_remove_color("10 20 30 40 50 60", "blue"), True)

    @weight(1)
    @visibility('after_due_date')
    def test_remove_color_4(self):
        self.assertEqual(check_remove_color("47\t47\t47", "red"), True)

    @weight(1)
    @visibility('after_due_date')
    def test_remove_color_5(self):
        self.assertEqual(check_remove_color("0 0 0", "green"), True)


    @weight(1)
    @visibility('after_due_date')
    def test_remove_color_6(self):
        self.assertEqual(check_remove_color("47  55  47 47  55  47 47  55  47 47  55  47", "blue"), True)

    @weight(1)
    @visibility('after_due_date')
    def test_remove_color_7(self):
        self.assertEqual(check_remove_color("", "red"), True)

    @weight(1)
    @visibility('after_due_date')
    def test_remove_color_8(self):
        self.assertEqual(check_remove_color("47 255 86 47 255 86 47 255 86", "green"), True)





