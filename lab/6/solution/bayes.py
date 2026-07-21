"""
CS51A - Assignment 7

Naive Bayes Model

Author: Zilong Ye
"""
SMALL_CONSTANT = 0.00009


def get_file_count(filename):
    """
    get a dictionary of {word: word_count} for the given file
    :param filename: (str) a file name
    :return: (dict) a dictionary of word and word count
    """
    word_dict = {}
    try:
        with open(filename, 'r') as file_in:
            for line in file_in:
                words = line.split()
                for word in words:
                    word_count = word_dict.get(word)
                    if not word_count:
                        word_dict.update({word: 1})
                    else:
                        word_dict.update({word: word_count + 1})
    except IOError:
        print("Could not open file " + filename)

    file_in.close()
    return word_dict


def counts_to_probs(counts, number):
    """
    convert counts to probabilities by dividing the given number
    :param counts: (dict) a given dictionary
    :param number: (int) a given number
    :return: (dict) a dictionary with words and their probs
    """
    for key, value in counts.items():
        counts.update({key: value / number})
    return counts


def get_num_lines(filename):
    """
    get the number of lines in the given file
    :param filename: (str) the given file
    :return: (int) the number of lines in the given file
    """
    file_in = open(filename, 'r')
    lines = file_in.readlines()
    return len(lines)


def train_model(filename):
    """
    get a dictionary with words and their probabilities
    :param filename: (str) a given file name
    :return: (dict) a dictionary of words and their probabilities
    """
    return counts_to_probs(get_file_count(filename), get_num_lines(filename))


def get_probability(model, review):
    """
    get the probability of the review given the model
    :param model: (dict) a dictionary of word probabilities
    :param review: (str) a given review sentence
    :return: (float) the review probability given the model
    """
    review_probability = 1
    for word in review.lower().split():
        word_probability = model.get(word)
        if not word_probability:
            review_probability *= SMALL_CONSTANT
        else:
            review_probability *= word_probability
    return review_probability


def classify(review, pos_model, neg_model):
    """
    classify the review to be positive or negative
    :param review: (str) a given review
    :param pos_model: (dict) the trained positive model
    :param neg_model: (dict) the trained negative model
    :return: (str) positive or negative
    """
    if get_probability(pos_model, review) >= get_probability(neg_model, review):
        return "positive"
    else:
        return "negative"


def sentiment_analyzer(pos_data, neg_data):
    """
    interact with user and conduct sentiment analysis of user input
    :param pos_data: (str) the file name of the positive training data
    :param neg_data: (str) the file name of the negative training data
    :return: none
    """
    pos_model = train_model(pos_data)
    neg_model = train_model(neg_data)
    print("Blank line terminates.")
    string = input("Enter a sentence: ")
    while string != "":
        print(classify(string, pos_model, neg_model))
        string = input("Enter a sentence: ")


def count_accurate_analysis(pos_model, neg_model, test_data, sentiment):
    """
    count the number of accurate analysis
    :param pos_model: (dict) the positive model
    :param neg_model: (dict) the negative model
    :param test_data: (str) the test data file
    :param sentiment: (str) "positive" or "negative"
    :return: (int) the count of accurate analysis
    """
    count = 0
    file = open(test_data, 'r')
    for line in file:
        if classify(line, pos_model, neg_model) == sentiment:
            count += 1
    file.close()
    return count


def get_accuracy(pos_test, neg_test, pos_train, neg_train):
    """
    evaluate the accuracy of the working model
    :param pos_test: (str) the positive test data
    :param neg_test: (str) the negative test data
    :param pos_train: (str) the positive training data
    :param neg_train: (str) the negative training data
    :return: none
    """
    # train the model
    pos_model = train_model(pos_train)
    neg_model = train_model(neg_train)

    # get the number of tests of positive, negative and total
    num_pos = get_num_lines(pos_test)
    num_neg = get_num_lines(neg_test)
    total = num_pos + num_neg

    # get the count of accurate sentiment analysis
    accurate_pos_count = count_accurate_analysis(pos_model, neg_model, pos_test, "positive")
    accurate_neg_count = count_accurate_analysis(pos_model, neg_model, neg_test, "negative")

    # print stats
    print("Positive accuracy:", accurate_pos_count / num_pos)
    print("Negative accuracy:", accurate_neg_count / num_neg)
    print("Total accuracy: ", (accurate_pos_count + accurate_neg_count) / total)


def main():
    # counts = get_file_count("simple.positive")
    # print(counts_to_probs(counts, 3))
    # print(get_num_lines("simple.positive"))
    # pos_model = train_model("simple.positive")
    # print(get_probability(pos_model, "I hated that class"))
    # pos_model = train_model("train.positive")
    # neg_model = train_model("train.negative")
    # print(classify("i kinda like it", pos_model, neg_model))
    # sentiment_analyzer("train.positive", "train.negative")
    print("Use train to model while test to evaluate")
    print('-' * 36)
    get_accuracy("test.positive", "test.negative", "train.positive", "train.negative")
    print()
    print("Use test to model while train to evaluate")
    print('-' * 36)
    get_accuracy("train.positive", "train.negative", "test.positive", "test.negative")

    # Evaluation discussion:
    #
    # Observation 1:
    #     Examples that are not accurate: "not good" which gives positive.
    # Reason: the model does not consider the correlation between words.
    #
    # Observation 2:
    #     Comparing the accuracy by switching training data and test data,
    #     we can see that the accuracy of positive analysis is similar, while the
    #     accuracy of negative analysis is quite different.
    # Reason: the size of negative test is too small, which may not be enough to
    #     well train a model, so the accuracy is low.


if __name__ == "__main__":
    main()
