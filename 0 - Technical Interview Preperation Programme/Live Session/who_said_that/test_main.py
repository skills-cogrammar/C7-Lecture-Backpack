import unittest
from main import remove_stop_words, to_lowercase

class TestMain(unittest.TestCase):
    def test_stop_words(self):
        input_sentence = "this is a test sentence."
        expected_output = "test sentence."
        self.assertEqual(remove_stop_words(input_sentence), expected_output)

    def test_lowercase_for_all(self):
        input_sentence = "THIS IS A TEST SENTENCE."
        expected_output = "this is a test sentence."
        self.assertEqual(to_lowercase(input_sentence), expected_output)


if __name__ == '__main__':
    unittest.main()