"""
CS51A - Assignment 7: Naive Bayes Sentiment Classifier

Author: arshtyi
Date: July 21, 2026

This program trains a Naive Bayes model from positive and negative review
files, classifies new reviews, and reports the model's accuracy.
"""


# A word absent from a training model receives this small probability.
UNKNOWN_WORD_PROBABILITY = 1 / 11000


# ---------------------------------------------------------------------------
# Training
# ---------------------------------------------------------------------------

def get_file_counts(filename):
    """Count how many times each word occurs in a review file.

    Each line of the file is one preprocessed review. Words are separated by
    whitespace, and duplicate words have already been removed from each line.

    :param filename: str, name of a file containing preprocessed reviews
    :return: dict mapping each word to its number of occurrences
    """
    word_counts = {}

    with open(filename, "r", encoding="utf-8") as review_file:
        for line in review_file:
            for word in line.split():
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1

    return word_counts


def counts_to_probs(counts, number):
    """Convert word counts into probabilities without changing ``counts``.

    :param counts: dict mapping words to occurrence counts
    :param number: int or float used as the denominator for every count
    :return: new dict mapping the same words to count / number
    """
    probabilities = {}

    for word in counts:
        probabilities[word] = counts[word] / number

    return probabilities


def count_lines(filename):
    """Count the number of examples (lines) in a review file.

    :param filename: str, name of a review file
    :return: int, number of lines in the file
    """
    number_of_lines = 0

    with open(filename, "r", encoding="utf-8") as review_file:
        for _ in review_file:
            number_of_lines += 1

    return number_of_lines


def train_model(filename):
    """Train a word-probability model from a file of labeled examples.

    :param filename: str, name of a positive or negative review file
    :return: dict mapping each word to p(word | file's label)
    """
    word_counts = get_file_counts(filename)
    number_of_examples = count_lines(filename)
    return counts_to_probs(word_counts, number_of_examples)


# ---------------------------------------------------------------------------
# Classifying
# ---------------------------------------------------------------------------

def get_probability(probability_dict, review):
    """Calculate a review's probability under one trained model.

    Words are lowercased and split on whitespace. A word that is not present
    in the model is assigned ``UNKNOWN_WORD_PROBABILITY``.

    :param probability_dict: dict mapping words to model probabilities
    :param review: str containing the review to evaluate
    :return: float, product of the review's individual word probabilities
    """
    review_probability = 1.0

    for word in review.lower().split():
        if word in probability_dict:
            review_probability *= probability_dict[word]
        else:
            review_probability *= UNKNOWN_WORD_PROBABILITY

    return review_probability


def classify(review, pos_model, neg_model):
    """Classify a review as positive or negative, with ties going positive.

    :param review: str containing the review to classify
    :param pos_model: dict of probabilities learned from positive examples
    :param neg_model: dict of probabilities learned from negative examples
    :return: str, either "positive" or "negative"
    """
    positive_probability = get_probability(pos_model, review)
    negative_probability = get_probability(neg_model, review)

    if positive_probability >= negative_probability:
        return "positive"
    else:
        return "negative"


def sentiment_analyzer(positive_exs, negative_exs):
    """Interactively classify sentences until the user enters a blank line.

    :param positive_exs: str, name of the positive training file
    :param negative_exs: str, name of the negative training file
    :return: None
    """
    pos_model = train_model(positive_exs)
    neg_model = train_model(negative_exs)

    print("Blank line terminates.")

    while True:
        review = input("Enter a sentence: ")

        if review == "":
            break

        print(classify(review, pos_model, neg_model))


# ---------------------------------------------------------------------------
# Evaluation
# ---------------------------------------------------------------------------

def count_correct_predictions(filename, expected_label,
                              pos_model, neg_model):
    """Count examples in a file that receive their expected label.

    :param filename: str, name of a test review file
    :param expected_label: str, correct label for every review in the file
    :param pos_model: dict of probabilities learned from positive examples
    :param neg_model: dict of probabilities learned from negative examples
    :return: int, number of correctly classified reviews
    """
    correct_predictions = 0

    with open(filename, "r", encoding="utf-8") as review_file:
        for review in review_file:
            prediction = classify(review, pos_model, neg_model)

            if prediction == expected_label:
                correct_predictions += 1

    return correct_predictions


def get_accuracy(pos_test, neg_test, pos_train, neg_train):
    """Train two models and print positive, negative, and total accuracy.

    :param pos_test: str, name of the positive test file
    :param neg_test: str, name of the negative test file
    :param pos_train: str, name of the positive training file
    :param neg_train: str, name of the negative training file
    :return: None
    """
    pos_model = train_model(pos_train)
    neg_model = train_model(neg_train)

    number_of_positive_tests = count_lines(pos_test)
    number_of_negative_tests = count_lines(neg_test)

    correct_positive = count_correct_predictions(
        pos_test, "positive", pos_model, neg_model
    )
    correct_negative = count_correct_predictions(
        neg_test, "negative", pos_model, neg_model
    )

    positive_accuracy = correct_positive / number_of_positive_tests
    negative_accuracy = correct_negative / number_of_negative_tests
    total_correct = correct_positive + correct_negative
    total_tests = number_of_positive_tests + number_of_negative_tests
    total_accuracy = total_correct / total_tests

    print("Positive accuracy:", positive_accuracy)
    print("Negative accuracy:", negative_accuracy)
    print("Total accuracy:", total_accuracy)


# ---------------------------------------------------------------------------
# Model evaluation
# ---------------------------------------------------------------------------

"""
Using test.positive and test.negative with the two training files produces:
Positive accuracy: 0.960431654676259
Negative accuracy: 0.708029197080292
Total accuracy: 0.9105339105339105
The total score is strong, but it hides a large difference between classes:
the model recognizes positive reviews much more reliably than negative ones.
The test set is also unbalanced (1,112 positive examples and 274 negative
examples), so the total accuracy is dominated by positive performance.

Two made-up counterexamples show the model's limitations. The positive review
"i love this bad movie" is labeled negative: its positive-model probability is
0.000402933034754337, just below its negative-model probability of
0.000412690973481078. Although "love" favors positive (0.113707 versus
0.031694), "bad" favors negative much more strongly (0.026255 versus
0.117026), and Naive Bayes cannot determine which word controls the sentence's
meaning. Conversely, the negative review "this is not good" is labeled
positive (0.00632461339364286 versus 0.00483599050334726). The positive model
gives "good" probability 0.157233 and "is" probability 0.488070, compared
with 0.119870 and 0.351077 in the negative model. Treating words independently
means it cannot understand that "not" negates "good".
"""


# ---------------------------------------------------------------------------
# Ethics reading response
# ---------------------------------------------------------------------------

"""
The GPT-4 overview describes a model that produces more natural text, follows
subtle instructions more reliably, handles much longer inputs, performs better
on many exams and reasoning tasks, and can interpret images as well as text.
These abilities support uses such as visual assistance, tutoring, coding, and
document analysis. However, GPT-4 can still hallucinate, reproduce bias, and
be pushed around safety barriers. Its fluent, humanlike answers may therefore
make users trust incorrect output, especially because little was disclosed
about its training data and construction.

The Osaka University work links fMRI measurements from people viewing images
to Stable Diffusion, reconstructing pictures with similar objects, layouts,
and colors. It is not unrestricted mind reading: the approach needs extensive
data from a particular person's brain and was trained to decode viewed images,
not private thoughts or dreams. It could eventually help neuroscience or give
people with paralysis another way to communicate. At the same time, improved
brain decoding could expose uniquely intimate information. Development should
therefore require informed and revocable consent, strict limits on collection
and reuse, strong data security, and laws against coerced scans. Those rules
should be established before the technology becomes portable or much easier
to train, rather than after mental privacy has already been harmed.
"""
