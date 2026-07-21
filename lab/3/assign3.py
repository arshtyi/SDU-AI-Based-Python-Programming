import random

from assign3_quotes import *


# ------------------------------------------------------------
# Movie Quotes Analysis Section


def is_question(text):
    """Return whether text ends with a question mark."""
    return text.endswith("?")


def get_first_quotes(quotes):
    """Return the first quote from every pair in quotes."""
    first_quotes = []

    for first_quote, response_quote in quotes:
        first_quotes.append(first_quote)

    return first_quotes


def get_first_questions(quotes):
    """Return all first quotes that are questions."""
    first_questions = []

    for first_quote in get_first_quotes(quotes):
        if is_question(first_quote):
            first_questions.append(first_quote)

    return first_questions


def count_question_quotes(quotes):
    """Return the number of first quotes that are questions."""
    return len(get_first_questions(quotes))


# There are 71,117 first quotes that are questions in the real data.


def get_average_question_length(quotes):
    """Return the average character length of all first questions."""
    first_questions = get_first_questions(quotes)

    if len(first_questions) == 0:
        return 0.0

    total_length = 0
    for question in first_questions:
        total_length += len(question)

    return total_length / len(first_questions)


# ------------------------------------------------------------
# Chatbot Section


def get_responses(quotes, question):
    """Return all responses paired with an exact first-quote match."""
    responses = []

    for first_quote, response_quote in quotes:
        if first_quote == question:
            responses.append(response_quote)

    return responses


def get_random_from_list(items):
    """Return a randomly selected element from items."""
    return random.choice(items)


def respond(quotes, question):
    """Return a random matching response, or an unknown-answer message."""
    responses = get_responses(quotes, question)

    if len(responses) == 0:
        return "I don't know."

    return get_random_from_list(responses)


def chatbot():
    """Run an interactive movie-quote chatbot until the user enters bye."""
    quotes = get_quotes()

    print("Welcome!")
    print("Ask me anything. When you're done, just type 'bye'")

    while True:
        user_input = input(" - ")
        normalized_input = user_input.lower()

        if normalized_input == "bye":
            break

        if is_question(normalized_input):
            print(respond(quotes, normalized_input))
        else:
            print("I only respond to questions!")


if __name__ == "__main__":
    chatbot()
