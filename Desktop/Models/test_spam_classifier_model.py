from spam_classifier_model import SpamClassifierModel
import unittest

class SpamClassifierModelTests(unittest.TestCase):

    def test_custom_tokenizer(self):
        model = SpamClassifierModel()
        text = "Did you catch the bus ? Are you frying an egg ? Did you make a tea? Are you eating your mom's left over dinner ? Do you feel my Love ?"
        actual = model._custom_tokenizer(text)
        expected = ['you', 'catch', 'bus', 'you', 'frying', 'egg', 'you', 'make', 'tea', 'you', 'eating', 'mom', 'left', 'dinner', 'you', 'feel', 'love']
        self.assertEqual(actual, expected)
    
    def test_predict(self):
        model = SpamClassifierModel()
        text = "Did you catch the bus ? Are you frying an egg ? Did you make a tea? Are you eating your mom's left over dinner ? Do you feel my Love ?"
        actual = model.predict(text)
        expected = "ham"
        self.assertEqual(actual, expected)


# This allows you to run the tests directly from the file
if __name__ == '__main__':
    unittest.main()      