from assign7 import *

import unittest
from gradescope_utils.autograder_utils.decorators import weight,visibility

        
model = {'a': 1.0, 'b': 1.6666666666666667, 'c': 0.3333333333333333} 

pos_model = {'i': 1.0, 'loved': 1.0, 'it': 0.6666666666666666, 
             'that': 0.6666666666666666, 
             'movie': 0.3333333333333333, 'hated': 0.3333333333333333}

neg_model = {'i': 1.0, 'hated': 1.0, 'that': 0.6666666666666666, 
             'movie': 0.3333333333333333, 
             'it': 0.6666666666666666, 'loved': 0.3333333333333333}


def check(submitted, answer):
    if submitted == answer:
        print("Passed")
    else:
        print("Failed. " + "Expected: " + str(answer) + " received " + \
              str(submitted))

    return submitted == answer

        
def check_float(submitted, answer, epsilon = 0.001):
    if abs(submitted-answer) < epsilon:
        print("Passed")
        return True
    else:
        print("Failed. " + "Expected: " + str(answer) + " received " + str(submitted))
        return False

    return abs(submitted-answer) < epsilon

        
def check_dictionary(submitted, answer):
    passed = True
    
    if len(submitted) != len(answer):
        passed = False
    else:
        for key in answer:
            if not (key in submitted):
                passed = False
            elif abs(submitted[key]-answer[key]) > 0.001:
                passed = False
        
    if passed:
        print("Passed")
    else:
        print("Failed. " + "Expected: " + str(answer) + " received " + \
              str(submitted)) 

    return passed


class Autograder(unittest.TestCase):
    
    @weight(3)
    @visibility('after_due_date')
    def test_get_file_counts(self):
        self.assertEqual(check_dictionary(get_file_counts("test.txt"), 
                                 {'a': 3, 'b': 5, 'c': 1}), True)
    
    @weight(3)
    @visibility('after_due_date')
    def test_train_model_and_counts_to_probs(self):
        self.assertEqual(check_dictionary(train_model("test.txt"), model), True)
    
    @weight(.5)
    def test_get_probability_1(self):
        self.assertEqual(check_float(get_probability(model, "a"), 1.0), True)
     
    @weight(.5) 
    @visibility('after_due_date')
    def test_get_probability_2(self):
        #checking lowercase
        self.assertEqual(check_float(get_probability(model, "A"), 1.0), True) 
    
    @weight(1)  
    @visibility('after_due_date') 
    def test_get_probability_3(self):
        self.assertEqual(check_float(get_probability(model, "d"), 1/11000), True)
    
    @weight(1) 
    @visibility('after_due_date')
    def test_get_probability_4(self):
        self.assertEqual(check_float(get_probability(model, "a b d a"),
                                     0.00015151515151515152), True)
        
    @weight(.5) 
    def test_classify_1(self):
        self.assertEqual(check(classify("i loved it", pos_model, neg_model),
                               "positive"), True)
    @weight(.5) 
    @visibility('after_due_date')
    def test_classify_2(self):
        self.assertEqual(check(classify("i hated it", pos_model, neg_model),
                               "negative"), True)
    @weight(.5) 
    @visibility('after_due_date')
    def test_classify_3(self):
        self.assertEqual(check(classify("i blah", pos_model, neg_model), 'positive'), True)
    
    @weight(.5) 
    @visibility('after_due_date')
    def test_classify_4(self):
        self.assertEqual(check(classify("hated blah", pos_model, neg_model), 'negative'), True)
        
    @weight(0) 
    @visibility('after_due_date')
    def test_get_accuracy(self):
        get_accuracy("test.positive", "test.negative", "train.positive", "train.negative")
        print("----- should look like -----")
        s = """Positive accuracy: 0.960431654676259
        Negative accuracy: 0.708029197080292
        Total accuracy: 0.9105339105339105"""
        print(s)
        self.assertEqual(True, True)
        
