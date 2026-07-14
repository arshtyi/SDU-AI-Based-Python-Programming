# NOTE: This file MUST be named test_SOMETHING, i.e. not SOMETHING_test
# And the functions in it must start with test_SOMETHING not SOMETHING_test
# if you want them to be run as tests (via auto-discovery)

import unittest
from gradescope_utils.autograder_utils.decorators import weight, visibility

# from password_checking import *

# def print_feedback(input):
#     print("INPUT: " + input)
#     print("EXPECTED: " + autograder_check_password(input))
#     print("RECEIVED: " + check_password(input))

# def autograder_check_password(password):
#     char_count = 0
#     lower_count = 0
#     upper_count = 0
#     digit_count = 0
#     special_count = 0

#     for c in password:
#         if c >= 'a' and c <= 'z':
#             lower_count += 1
#         elif c >= 'A' and c <= 'Z':
#             upper_count += 1
#         elif str.isdigit(c):
#             digit_count += 1
#         elif c == '!' or c == '@' or c == '#' or c == '$':
#             special_count += 1
        
#         char_count += 1

#     if char_count < 8:
#         return "Password should contain at least 8 characters"
#     elif lower_count < 2:
#         return "Password should contain at least 2 lowercase letter"
#     elif upper_count < 1:
#         return "Password should contain at least 1 uppercase letter"
#     elif digit_count < 2:
#         return "Password should contain at least 2 numbers"
#     elif special_count == 0:
#         return "Password should contain at least 1 of the characters !@#$"
#     else:
#         return "Password " + password + " is a valid password"


# class Autograder(unittest.TestCase):
#     # password doesn't have at least 8 characters
#     @weight(1)
#     def test_invalid_1(self):
#         if "8 characters" not in check_password("11aaB!"):
#             print_feedback("11aaB!")
#         self.assertEqual("8 characters" in check_password("11aaB!"), True)

#     @weight(1)
#     @visibility('after_due_date')
#     def test_invalid_2(self):
#         if "8 characters" not in check_password(""):
#             print_feedback("")
#         self.assertEqual("8 characters" in check_password(""), True)

#     # password doesn't have at least 2 lower case letters
#     @weight(1)
#     @visibility('after_due_date')
#     def test_invalid_3(self):
#         if "2 lowercase" not in check_password("123aABCD!"):
#             print_feedback("123aABCD!")
#         self.assertEqual("2 lowercase" in check_password("123aABCD!"), True)

#     # password doesn't have at least 1 upper case letter
#     @weight(1)
#     @visibility('after_due_date')
#     def test_invalid_4(self):
#         if "1 uppercase" not in check_password("123abcd!"):
#             print_feedback("123abcd!")
#         self.assertEqual("1 uppercase" in check_password("123abcd!"), True)

#     # password doesn't have at least 2 numbers
#     @weight(1)
#     @visibility('after_due_date')
#     def test_invalid_5(self):
#         if "2 numbers" not in check_password("1abcDEF!"):
#             print_feedback("1abcDEF!")
#         self.assertEqual("2 numbers" in check_password("1abcDEF!"), True)

#     # password doesn't have at least 1 special character
#     @weight(1)
#     @visibility('after_due_date')
#     def test_invalid_6(self):
#         if "!@#$" not in check_password("123abcDEF"):
#             print_feedback("123abcDEF")
#         self.assertEqual("!@#$" in check_password("123abcDEF"), True)

#     @weight(1)
#     @visibility('after_due_date')
#     def test_invalid_7(self):
#         if "!@#$" not in check_password("123abcDEF^"):
#             print_feedback("123abcDEF^")
#         self.assertEqual("!@#$" in check_password("123abcDEF^"), True)


#     # valid password
#     @weight(1)
#     def test_valid_1(self):
#         if "is a valid password" not in check_password("123abcDEF$"):
#             print_feedback("123abcDEF$")
#         self.assertEqual("is a valid password" in check_password("123abcDEF$"), True)

#     @weight(1)
#     @visibility('after_due_date')
#     def test_valid_2(self):
#         if "is a valid password" not in check_password("12abDD$!"):
#             print_feedback("12abDD$!")
#         self.assertEqual("is a valid password" in check_password("12abDD$!"), True)

#     @weight(1)
#     @visibility('after_due_date')
#     def test_valid_3(self):
#         if "is a valid password" not in check_password("123456abcdefDEFGHI!@#$"):
#             print_feedback("123456abcdefDEFGHI!@#$")
#         self.assertEqual("is a valid password" in check_password("123456abcdefDEFGHI!@#$"), True)




