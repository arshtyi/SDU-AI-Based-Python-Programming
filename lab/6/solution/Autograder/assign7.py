"""
Max Zonana
CS51A
assignment 7
3-21-23
"""


def get_file_counts(filename):
    """
    get word frequencies
    :param filename: file containing data
    :return: (dict) with words and their frequencies
    """

    word_dict = {}
    file = open(filename, "r")

    # splits each line into words
    for line in file:
        new_line = line.split()
        # adds words to dict
        for key in new_line:
            if key not in word_dict:
                word_dict[key] = 1
            else:
                word_dict[key] += 1

    file.close()
    return word_dict


def counts_to_probs(your_dict, dividing_number):
    """
    divide frequency by a number
    :param your_dict: (dict)
    :param dividing_number: (int) number to divide with
    :return: (dict) with divided frequencies
    """

    probs_dict = {}

    # divides each value by dividing number
    for key in your_dict:
        probs_dict[key] = your_dict[key] / dividing_number

    return probs_dict


def train_model(filename):
    """
    showing the probabilities of words in model
    :param filename: (file)
    :return: (dict) with probabilities
    """

    number_of_lines = 0
    file = open(filename, 'r')

    # counts how many lines there are
    for _ in file:
        number_of_lines += 1

    final_dict = counts_to_probs(get_file_counts(filename), number_of_lines)

    file.close()
    return final_dict


def get_probability(probability_dict, review):
    """
    probability of review is positive or negative
    :param probability_dict: (dict) with the probability of words
    :param review: (str) a sentence
    :return: (int) probability
    """

    total_probability = 1
    words = review.lower().split()

    # calculates the probability of each word
    for word in words:
        if word in probability_dict:
            total_probability = total_probability * probability_dict[word]
        else:
            total_probability = total_probability * 1/11000

    return total_probability


def classify(review, pos_model, neg_model):
    """
    either says the review is positive or negative
    :param review: (str) a sentence
    :param pos_model:
    :param neg_model:
    :return: (str) "positive" or "negative"
    """

    # checks which probability of the review being positive or negative is higher
    if get_probability(pos_model, review) >= get_probability(neg_model, review):
        return "positive"
    else:
        return "negative"


def sentiment_analyzer(positive_exs, negative_exs):
    """
    interactive to determine if user input is pos/neg
    :param positive_exs: (file) examples of positive sentiments
    :param negative_exs: (file) examples of negative sentiments
    :return: (str) "positive" or "negative" unless no input when it ends
    """

    pos_model = train_model(positive_exs)
    neg_model = train_model(negative_exs)
    print("Blank line terminates.")
    review = input("Enter a sentence: ")

    # a loop allowing users to input as many reviews they want
    while review != "":
        print(classify(review, pos_model, neg_model))
        review = input("Enter a sentence: ")


def file_lines(filename):
    """
    counts number of lines in file
    :param filename: (file)
    :return: (int) representing number of lines
    """

    file = open(filename, "r")
    lines = 0

    # counts how many lines there are
    for _ in file:
        lines += 1

    return lines


def get_accuracy(positive_file, negative_file, positive_trainer, negative_trainer):
    """
    how accurate it classifies positive or negative reviews
    :param positive_file: (file) of positive reviews
    :param negative_file: (file) of negative reviews
    :param positive_trainer: (file) to train the positive model
    :param negative_trainer: (file) to train the positive model
    :return:(str) positive, negative and total accuracies
    """

    trained_positive = train_model(positive_trainer)
    trained_negative = train_model(negative_trainer)
    total_positive_reviews = file_lines(positive_file)
    total_negative_reviews = file_lines(negative_file)
    guessed_positive_reviews = 0
    guessed_negative_reviews = 0

    # sees if the model recognizes positive reviews as such
    for review in positive_file:
        if classify(review, trained_positive, trained_negative) == "positive":
            guessed_positive_reviews += 1

    # sees if the model recognizes negative reviews as such
    for review in negative_file:
        if classify(review, trained_positive, trained_negative) == "negative":
            guessed_negative_reviews += 1

    print("Positive accuracy: " + str(guessed_positive_reviews / total_positive_reviews))
    print("Negative accuracy: " + str(guessed_negative_reviews / total_negative_reviews))
    print("Total accuracy: " + str((guessed_positive_reviews + guessed_negative_reviews) / (total_positive_reviews +
                                                                                            total_negative_reviews)))
