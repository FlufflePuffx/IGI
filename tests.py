import unittest
import parser


class TestSentencesAmount(unittest.TestCase):
    def test_sample(self):
        text = 'Education never ends, Watson. It is a series of lessons, with the greatest for the last.'
        expected = 2
        actual = parser.count_sentences(text)
        self.assertEqual(actual, expected, 'sample test is not passed. your result: ' + str(actual))

    def test_non_declarative(self):
        text = 'There is nothing more deceptive than an obvious fact. How do you think?'
        expected = 1
        actual = parser.count_non_declarative_sentences(text)
        self.assertEqual(actual, expected, 'non_declarative test is not passed')

    def test_with_abbreviations(self):
        text = 'Dr. Holmes, they were the footprints of a gigantic hound!'
        expected = 1
        actual = parser.count_sentences(text.lower())
        self.assertEqual(actual, expected, 'abbreviations test is not passed. your result: ' + str(actual))


class TestAverageSentenceLength(unittest.TestCase):
    def test_sample_text(self):
        text = 'My name is Sherlock Holmes. It is my business to know what other people do not know.'
        expected = round(66 / 2, 2)
        actual = parser.average_sentence_length(text)
        self.assertEqual(actual, expected, 'av length test is not passed. your result: ' + str(actual))

    def test_with_numbers(self):
        text = 'I see 1000000 of stars, Holmes, says Watson.'
        expected = round(27 / 1, 2)
        actual = parser.average_sentence_length(text)
        self.assertEqual(actual, expected, 'av length with numbers is not passed. your result: ' + str(actual))


class TestAvgWordLength(unittest.TestCase):
    def test_sample_text(self):
        text = 'And what do you conclude from that, Watson?'
        expected = round(34 / 8, 2)
        actual = parser.average_word_length(text)
        self.assertEqual(actual, expected, 'av word length is not passed. your result: ' + str(actual))

    def test_with_numbers(self):
        text = 'Watson, you id1ot! Someone has stolen our tent 2 days ago!'
        expected = round(44 / 10, 2)
        actual = parser.average_word_length(text)
        self.assertEqual(actual, expected, 'av word length test with numbers is not passed. your result: ' + str(actual))


class TestTopKnGrams(unittest.TestCase):
    def test_sample_text(self):
        text = 'I am the most incurably lazy devil that ever stood in the most leather shoe! And I am tired.'
        expected = [('i am', 2), ('the most', 2)]
        actual = parser.top_k_repeated_n_grams(text, 2, 2)
        self.assertEqual(actual, expected, 'ngrams test is not passed, your result: ' + str(actual))

    def test_text_without_repeated_anagrams(self):
        text = 'To a great mind, nothing is little, remarked Holmes.'
        expected = [('to a great', 1), ('a great mind', 1), ('great mind nothing', 1)]
        actual = parser.top_k_repeated_n_grams(text, 3, 3)
        self.assertEqual(actual, expected, 'ngrams test is not passed, your result: ' + str(actual))
