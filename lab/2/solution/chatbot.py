"""
CS51A - Assignment 3

Implement a Chatbot using knowledge of lists, sequences

Author: Zilong Ye
"""
from random import *
from assign3_quotes import *


def is_question(string):
    """
    check if the input <string> is a question

    :param string: (str) an input sentence
    :return: (boolean) True if the input is a question (e.g., end with ?)
    """
    return string[-1] == "?"


def get_first_quotes(quotes):
    """
    get the first quotes from the given <list_of_quotes>

    :param quotes: (list) a list of quotes
    :return: (list) a list of first quotes from the given dataset
    """
    first_quotes = []
    for pair in quotes:
        first_quotes.append(pair[0])
    return first_quotes


def get_first_questions(quotes):
    """
    get the list of first quotes that are questions

    :param quotes: (list) a list of quotes
    :return: (list) a list of first quotes that are questions
    """
    first_questions = []
    for pair in quotes:
        if is_question(pair[0]):
            first_questions.append(pair[0])
    return first_questions


def count_question_quotes(quotes):
    """
    count the number of first quotes that are questions

    :param quotes: (list) a list of quotes
    :return: (int) the number of first quotes that are questions
    """
    return len(get_first_questions(quotes))


def get_average_question_length(quotes):
    """
    get the average length of the first quotes that are questions

    :param quotes: (list) a list of quotes
    :return: (float) the average length of the first quotes that are questions
    """
    question_length = 0
    for question in get_first_questions(quotes):
        question_length += len(question)
    return question_length / count_question_quotes(quotes)


def get_responses(quotes, question):
    """
    get the second entries from the quotes whose first entry mathces the question

    :param quotes: (list) a list of quotes
    :param question: (str) a question
    :return: (list) a list of answers that match the question
    """
    responses = []
    for pair in quotes:
        if pair[0] == question:
            responses.append(pair[1])
    return responses


def get_random_from_list(responses):
    """
    get a random response from the given list of responses

    :param responses: (list) a list of responses
    :return: (str) a random response from the given list
    """
    return choice(responses)


def respond(quotes, question):
    """
    respond to a user input question

    :param quotes: (list) a list of quotes
    :param question: (str) the user input question
    :return: (str) either the answers matches the question or "don't know"
    """
    if not get_responses(quotes, question):
        return "I don't know"
    else:
        return get_random_from_list(get_responses(quotes, question))


def chatbot():
    """
    the chatbot

    :return: none
    """
    print("Welcome to Chatbot!\n"
          "When you are done, just type 'bye'")

    question = input("- ")
    quotes = get_quotes()

    while question != "bye":
        print(respond(quotes, question))
        question = input("- ")

    print("Bye! See you next time!")


def main():
    # print(get_first_quotes(get_quotes()))
    # print(get_first_questions(get_quotes()))
    # print(count_question_quotes(get_quotes()))
    # print(get_average_question_length(get_quotes()))
    # print(get_responses(get_practice_quotes(), "what is your name?"))
    # print(get_random_from_list(["apple", "orange", "banana"]))
    # print(respond(get_practice_quotes(), ""))
    chatbot()


if __name__ == "__main__":
    main()


