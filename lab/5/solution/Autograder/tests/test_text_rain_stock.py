# NOTE: This file MUST be named test_SOMETHING, i.e. not SOMETHING_test
# And the functions in it must start with test_SOMETHING not SOMETHING_test
# if you want them to be run as tests (via auto-discovery)

import unittest
from gradescope_utils.autograder_utils.decorators import weight, visibility

from stock_rain import *

class Autograder(unittest.TestCase):
    # test parse_rainfall
    @weight(1)
    def test_parse_rainfall_1(self):
        self.assertEqual(parse_rainfall("csvs/rainTest1.csv"), {'2012-01-03': 0.03, '2012-01-04': 0.8, '2012-01-05': 0.05,
           '2012-01-06': 0.1, '2012-01-09': 0.17})

    @weight(1)
    def test_parse_rainfall_2(self):
        self.assertEqual(parse_rainfall("csvs/rainTest2.csv"), {'2012-01-03': 0.03, '2012-01-04': 0.8, '2012-01-05': 0.05,
           '2012-01-06': 0.1, '2012-01-10': 0.05})

    @weight(0.5)
    def test_parse_rainfall_3(self):
        self.assertEqual(parse_rainfall("csvs/rainTest3.csv"), {'2012-01-01': 0.0, '2012-01-02': 0.43, '2012-01-03': 0.03,
           '2012-01-04': 0.8, '2012-01-05': 0.05, '2012-01-06': 0.1,
           '2012-01-07': 0.0, '2012-01-08': 0.0, '2012-01-09': 0.17,
           '2012-01-10': 0.0, '2012-01-11': 0.17})

    @weight(0.5)
    def test_parse_rainfall_4(self):
        self.assertEqual(parse_rainfall("csvs/rainTest4.csv"), {'2012-01-01': 0.0, '2012-01-02': 0.43, '2012-01-03': 0.03,
          '2012-01-04': 0.8, '2012-01-05': 0.05, '2012-01-06': 0.1,
          '2012-01-07': 0.0, '2012-01-08': 0.0, '2012-01-09': 0.17,
          '2012-01-10': 0.0, '2012-01-11': 0.17})

    # @weight(0.5)
    # def test_parse_rainfall_5(self):
    #     self.assertEqual(parse_rainfall("csvs/rainTest5.csv"), {'2012-01-01': 0.0, '2012-01-02': 0.43, '2012-01-03': 0.03,
    #       '2012-01-04': 0.8, '2012-01-05': 0.05, '2012-01-06': 0.1,
    #       '2012-01-07': 0.0, '2012-01-08': 0.0, '2012-01-09': 0.17})

    # @weight(0.5)
    # def test_parse_rainfall_6(self):
    #     self.assertEqual(parse_rainfall("csvs/rainTest6.csv"), {'2012-01-01': 0.0, '2012-01-02': 0.43, '2012-01-03': 0.03,
    #       '2012-01-04': 0.8, '2012-01-05': 0.05, '2012-01-06': 0.1,
    #       '2012-01-07': 0.0, '2012-01-08': 0.0, '2012-01-09': 0.17})

    @weight(0.5)
    def test_parse_rainfall_7(self):
        self.assertEqual(parse_rainfall("csvs/rainTest7.csv"), {'2012-01-01': 0.0, '2012-01-02': 0.43, '2012-01-04': 0.8,
           '2012-01-05': 0.05, '2012-01-06': 0.1, '2012-01-08': 0.0,
           '2012-01-09': 0.17})

    @weight(0.5)
    def test_parse_rainfall_8(self):
        self.assertEqual(parse_rainfall("csvs/rainTest8.csv"), {'2012-01-02': 0.43, '2012-01-04': 0.8, '2012-01-05': 0.05,
           '2012-01-06': 0.1, '2012-01-07': 0.0, '2012-01-08': 0.0})

    @weight(0.5)
    def test_parse_rainfall_9(self):
        self.assertEqual(parse_rainfall("csvs/rainTest9.csv"), {'2012-01-01': 0.0, '2012-01-03': 0.03, '2012-01-05': 0.05,
           '2012-01-07': 0.0, '2012-01-09': 0.17})

    @weight(0.5)
    def test_parse_rainfall_10(self):
        self.assertEqual(parse_rainfall("csvs/rainTest10.csv"), {'2012-01-09': 0.17})


    # test parse_stock
    @weight(0.5)
    def test_parse_stock_1(self):
        self.assertEqual(parse_stock("csvs/stockTest1.csv", "GOOGL"), {'2012-01-03': 6.24, '2012-01-04': 1.62, '2012-01-05': -1.57,
          '2012-01-06': -4.56, '2012-01-09': -12.03})

    @weight(0.5)
    def test_parse_stock_2(self):
        self.assertEqual(parse_stock("csvs/stockTest2.csv", "GOOGL"), {'2012-01-03': 6.24, '2012-01-04': 1.62, '2012-01-05': -1.57,
          '2012-01-06': -4.56, '2012-01-10': -12.03})

    @weight(0.5)
    def test_parse_stock_3(self):
        self.assertEqual(parse_stock("csvs/stockTest3.csv", "GOOGL"), {'2013-01-03': 6.24, '2013-01-04': 1.62, '2013-01-05': -1.57,
          '2013-01-06': -4.56, '2013-01-09': -12.03, '2013-01-10': -4.56, '2013-01-11': -12.03})

    @weight(0.5)
    def test_parse_stock_5(self):
        self.assertEqual(parse_stock("csvs/stockTest5.csv", "GOOGL"), {'2012-01-03': 6.24, '2012-01-04': 1.62, '2012-01-05': -1.57,
          '2012-01-06': -4.56, '2012-01-09': -12.03})

    @weight(0.5)
    def test_parse_stock_6(self):
        self.assertEqual(parse_stock("csvs/stockTest6.csv", "GOOGL"), {'2012-01-03': 6.24, '2012-01-04': 1.62, '2012-01-05': -1.57,
          '2012-01-06': -4.56, '2012-01-09': -12.03})

    @weight(0.5)
    def test_parse_stock_7(self):
        self.assertEqual(parse_stock("csvs/stockTest7.csv", "MRK"), {'2006-01-03': 0.23})

    @weight(0.5)
    def test_parse_stock_8(self):
        self.assertEqual(parse_stock("csvs/stockTest7.csv", "AAPL"), {'2006-01-03': 0.34})

    @weight(0.5)
    def test_parse_stock_9(self):
        self.assertEqual(parse_stock("csvs/stockTest7.csv", "AXP"), {'2006-01-03': 0.88})

    @weight(1)
    def test_parse_stock_10(self):
        self.assertEqual(parse_stock("csvs/stockTest9.csv", "GOOGL"), {'2012-01-05': -1.57, '2012-01-06': -4.56, '2012-01-09': -12.03})
    
    
    # test correlate_data
    @weight(1)
    def test_correlate_data_1(self):
        self.assertEqual(correlate_data({'2012-01-03': 6.24, '2012-01-04': 1.62, '2012-01-05': -1.57,
          '2012-01-06': -4.56},
         {'2012-01-03': 0.03, '2012-01-04': 0.8, '2012-01-05': 0.05,
          '2012-01-06': 0.1}), [[6.24, 0.03], [1.62, 0.8], [-1.57, 0.05], [-4.56, 0.1]])

    @weight(1)
    @visibility('after_due_date')
    def test_correlate_data_2(self):
        self.assertEqual(correlate_data({'2012-01-03': 6.24, '2012-01-04': 1.62, '2012-01-05': -1.57,
          '2012-01-06': -4.56, '2012-01-09': -12.03},
         {}), 
          [])

    @weight(1)
    @visibility('after_due_date')
    def test_correlate_data_3(self):
        self.assertEqual(correlate_data({},
         {'2012-01-03': 0.03, '2012-01-04': 0.8, '2012-01-05': 0.05,
          '2012-01-06': 0.1, '2012-01-10': 0.05}), 
          [])

    @weight(1)
    @visibility('after_due_date')
    def test_correlate_data_4(self):
        self.assertEqual(correlate_data({'2012-01-03': 6.24, '2012-01-04': 1.62, '2012-01-05': -1.57,
          '2012-01-06': -4.56, '2012-01-09': -12.03, '2012-01-10': -12.03,
          '2012-02-10': -4.56, '2012-02-09': -12.03},
         {'2012-01-03': 0.03, '2012-01-04': 0.8, '2012-01-05': 0.05,
          '2012-01-06': 0.1, '2012-01-10': 0.05}), 
          [[6.24, 0.03], [1.62, 0.8], [-1.57, 0.05], [-4.56, 0.1], [-12.03, 0.05]])

    @weight(1)
    @visibility('after_due_date')
    def test_correlate_data_5(self):
        self.assertEqual(correlate_data({'2012-01-03': 6.24, '2012-01-04': 1.62, '2012-01-05': -1.57,
          '2012-01-06': -4.56, '2012-01-09': -12.03, '2012-01-10': -4.56},
         {'2012-01-03': 0.03, '2012-01-04': 0.8, '2012-01-05': 0.05,
          '2012-01-06': 0.1, '2012-01-09': 0.17, '2012-01-10': 0.0,
          '2012-01-11': 0.17}), 
          [[6.24, 0.03], [1.62, 0.8], [-1.57, 0.05], [-4.56, 0.1],
          [-12.03, 0.17], [-4.56, 0.0]])

    @weight(1)
    @visibility('after_due_date')
    def test_correlate_data_6(self):
        self.assertEqual(correlate_data({'2012-01-13': 6.24, '2012-02-14': 1.62, '2012-01-15': -1.57,
          '2012-01-16': -4.56, '2012-01-19': -12.03, '2012-01-20': -4.56,
          '2012-02-10': -4.56, '2012-02-09': -12.03},
         {'2012-01-01': 0.0, '2012-01-02': 0.43, '2012-01-03': 0.03,
          '2012-01-04': 0.8, '2012-01-05': 0.05, '2012-01-06': 0.1,
          '2012-01-07': 0.0, '2012-01-08': 0.0, '2012-01-09': 0.17,
          '2012-01-10': 0.0, '2012-01-11': 0.17}), 
          [])

    @weight(1)
    @visibility('after_due_date')
    def test_correlate_data_7(self):
        self.assertEqual(correlate_data({'2012-01-03': 6.24, '2012-02-04': 1.62, '2012-01-05': -1.57,
          '2012-01-06': -4.56, '2012-01-09': -12.03, '2012-01-10': -4.56,
          '2012-02-10': -4.56, '2012-02-09': -12.03},
         {'2013-01-01': 0.0, '2013-01-02': 0.43, '2013-01-03': 0.03,
          '2013-01-04': 0.8, '2013-01-05': 0.05, '2013-01-06': 0.1,
          '2013-01-07': 0.0, '2013-01-08': 0.0, '2013-01-09': 0.17,
          '2013-01-10': 0.0, '2013-01-11': 0.17}), 
          [])

    @weight(1)
    @visibility('after_due_date')
    def test_correlate_data_8(self):
        self.assertEqual(correlate_data({'2012-01-03': 6.24, '2012-02-04': 1.62, '2012-01-05': -1.57,
          '2012-01-06': -4.56, '2012-01-09': -12.03, '2012-01-10': -4.56,
          '2012-02-10': -4.56, '2012-02-09': -12.03},
         {'2012-01-03': 0.03, '2012-01-04': 0.8, '2012-01-05': 0.05,
          '2012-01-06': 0.1, '2012-01-09': 0.17}), 
          [[6.24, 0.03], [-1.57, 0.05], [-4.56, 0.1], [-12.03, 0.17]])

    @weight(1)
    @visibility('after_due_date')
    def test_correlate_data_9(self):
        self.assertEqual(correlate_data({'2012-01-03': 6.24, '2012-02-04': 1.62, '2012-01-05': -1.57,
          '2012-01-06': -4.56, '2012-01-09': -12.03, '2012-01-10': -4.56,
            '2012-02-10': -4.56, '2012-02-09': -12.03},
         {'2012-01-03': 0.03, '2012-01-04': 0.8, '2012-01-05': 0.05,
           '2012-01-06': 0.1, '2012-01-10': 0.05}), 
          [[6.24, 0.03], [-1.57, 0.05], [-4.56, 0.1], [-4.56, 0.05]])

    @weight(1)
    @visibility('after_due_date')
    def test_correlate_data_10(self):
        self.assertEqual(correlate_data({'2012-01-03': 6.24, '2012-02-04': 1.62, '2012-01-05': -1.57,
          '2012-01-06': -4.56, '2012-01-09': -12.03, '2012-01-10': -4.56,
          '2012-02-10': -4.56, '2012-02-09': -12.03},
         {'2012-01-01': 0.0, '2012-01-02': 0.43, '2012-01-03': 0.03,
           '2012-01-04': 0.8, '2012-01-05': 0.05, '2012-01-06': 0.1,
           '2012-01-07': 0.0, '2012-01-08': 0.0, '2012-01-09': 0.17,
           '2012-01-10': 0.0, '2012-01-11': 0.17}), 
          [[6.24, 0.03], [-1.57, 0.05], [-4.56, 0.1], [-12.03, 0.17], [-4.56, 0.0]])



