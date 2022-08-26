import unittest

# Compute follow inputs: £0-50, £2-, £10-, (£100- for extra marks)

class RunTestCase(unittest.TestCase): 
    # @unittest.skip('Coin tests not run')
    def test_coin_class_fifty_pence(self):
        test = '£0-50'
        expected_result = 271
        combinations = Coins(test)
        self.assertEqual(combinations(), expected_result)

    # @unittest.skip('Coin tests not run')
    def test_coin_class_two_pounds(self):
        test = '£2-00'
        expected_result = 70407
        combinations = Coins(test)
        self.assertEqual(combinations(), expected_result)

    # @unittest.skip('Coin tests not run')
    def test_coin_class_ten_pounds(self):
        test = '£10-00'
        expected_result = 317476425
        combinations = Coins(test)
        self.assertEqual(combinations(), expected_result)

unittest.main(argv=[''], verbosity=2, exit=False)
