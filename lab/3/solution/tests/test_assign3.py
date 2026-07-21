# NOTE: This file MUST be named test_SOMETHING, i.e. not SOMETHING_test
# And the functions in it must start with test_SOMETHING not SOMETHING_test
# if you want them to be run as tests (via auto-discovery)

import unittest
from gradescope_utils.autograder_utils.decorators import weight, visibility

from assign3 import *

test = [("a?", "a"),
        ("b?", "b"),
        ("a?", "a2"),
        ("a?", "a3"),
        ("b?", "b2"),
        ("c?", "c")]


def check_get_responses():
    # get_responses ---------------
    if get_responses(test, "a?") == ["a", "a2", "a3"]:
        print("get_response: PASS")
        return True
    else:
        print("get_response: FAIL")
        print('Input: [("a?", "a"), ("b?", "b"), ("a?", "a2"), ("a?", "a3"), ("b?", "b2"), ("c?", "c")]')
        print("Expected: ", '["a", "a2", "a3"]')
        return False


def check_respond():
    passed = True

    if not respond(test, "a?").startswith("a"):
        passed = False
        print("respond failed question check: ")
        print('Input: [("a?", "a"), ("b?", "b"), ("a?", "a2"), ("a?", "a3"), ("b?", "b2"), ("c?", "c")]')
        print("Question: a?")
        print("Expected: one item from a, or a2 or a3")

    if not respond(test, "d?") == "I don't know.":
        passed = False
        print("respond failed 'I don't know.' check: ")
        print('Input: [("a?", "a"), ("b?", "b"), ("a?", "a2"), ("a?", "a3"), ("b?", "b2"), ("c?", "c")]')
        print("Question: d?")
        print("Expected: I don't know.")

    if passed:
        print("respond: PASS")

    return passed


class Autograder(unittest.TestCase):
    @weight(1)
    def test_is_question_1(self):
        if is_question("do you want some pie?") != True:
            print("Input: " + "do you want some pie?")
            print("Expected: True")
        self.assertEqual(is_question("do you want some pie?"), True)
        

    @weight(1)
    @visibility('after_due_date')
    def test_is_question_2(self):
        if is_question("of course!") != False:
            print("Input: " + "of course!")
            print("Expected: False")
        self.assertEqual(is_question("of course!"), False)
        

    @weight(1.5)
    def test_get_first_quotes_1(self):
        simple_quotes = get_practice_quotes()
        if get_first_quotes(simple_quotes) != ["quote1", "first", "first they said this", "what?", "what?"]:
            print('Input: practice_quotes from the handout')
            print('Expected: ["quote1", "first", "first they said this", "what?", "what?"]')
        self.assertEqual(get_first_quotes(simple_quotes) == ["quote1", "first", "first they said this", "what?", "what?"], True)

    @weight(1.5)
    @visibility('after_due_date')
    def test_get_first_quotes_2(self):
        if get_first_quotes(test) != ["a?", "b?", "a?", "a?", "b?", "c?"]:
            print('Input: [("a?", "a"), ("b?", "b"), ("a?", "a2"), ("a?", "a3"), ("b?", "b2"), ("c?", "c")]')
            print('Expected: ["a?", "b?", "a?", "a?", "b?", "c?"]')
        self.assertEqual(get_first_quotes(test) == ["a?", "b?", "a?", "a?", "b?", "c?"], True)

    @weight(1)
    def test_get_first_questions_1(self):
        simple_quotes = get_practice_quotes()
        if get_first_questions(simple_quotes) != ["what?", "what?"]:
            print('Input: practice_quotes from the handout')
            print('Expected: ["what?", "what?"]')
        self.assertEqual(get_first_questions(simple_quotes) == ["what?", "what?"], True)

    @weight(1)
    @visibility('after_due_date')
    def test_get_first_questions_2(self):
        if get_first_questions(test) != ["a?", "b?", "a?", "a?", "b?", "c?"]:
            print('Input: [("a?", "a"), ("b?", "b"), ("a?", "a2"), ("a?", "a3"), ("b?", "b2"), ("c?", "c")]')
            print('Expected: ["a?", "b?", "a?", "a?", "b?", "c?"]')
        self.assertEqual(get_first_questions(test) == ["a?", "b?", "a?", "a?", "b?", "c?"], True)

    @weight(1)
    def test_count_question_quotes(self):
        simple_quotes = get_practice_quotes()
        if count_question_quotes(simple_quotes) != 2:
            print("Input: practice_quotes from the handout")
            print("Expected: 2")
        self.assertEqual(count_question_quotes(simple_quotes), 2)

    @weight(1.5)
    def test_get_average_question_length_1(self):
        simple_quotes = get_practice_quotes()
        if get_average_question_length(simple_quotes) != 5:
            print("Input: practice_quotes from the handout")
            print("Expected: 5")
        self.assertEqual(get_average_question_length(simple_quotes), 5)

    @weight(1.5)
    @visibility('after_due_date')
    def test_get_average_question_length_2(self):
        if get_average_question_length(test) != 2:
            print('Input: [("a?", "a"), ("b?", "b"), ("a?", "a2"), ("a?", "a3"), ("b?", "b2"), ("c?", "c")]')
            print("Expected: 2")
        self.assertEqual(get_average_question_length(test), 2)

    @weight(3)
    @visibility('after_due_date')
    def test_get_responses(self):
        self.assertEqual(check_get_responses(), True)

    @weight(3)
    @visibility('after_due_date')
    def test_respond(self):
        self.assertEqual(check_respond(), True)
