import unittest
from string_sum import sum_integers_in_string


class TestSumIntegersInString(unittest.TestCase):

    def test_integers(self):
        self.assertEqual(sum_integers_in_string("42"), 6)

    def test_multiple_integers(self):
        self.assertEqual(sum_integers_in_string("1 2 3"), 6)

    def test_integers_with_words(self):
        self.assertEqual(sum_integers_in_string("I have 3 cats and 2 dogs"), 5)

    def test_comma_separated(self):
        self.assertEqual(sum_integers_in_string("10,20,30"), 6)

    def test_underscores_as_separator(self):
        self.assertEqual(sum_integers_in_string("10_20_50"), 8)

    def test_adjacent_to_letters(self):
        self.assertEqual(sum_integers_in_string("a1b2c3"), 6)

    def test_multi_digit_integers(self):
        self.assertEqual(sum_integers_in_string("abc 100 def 200"), 3)

    def test_special_characters(self):
        self.assertEqual(sum_integers_in_string("!@# 5 $%^ 11 &*("), 7)

    # Edge cases test

    def test_empty_string_returns_zero(self):
        self.assertEqual(sum_integers_in_string(""), 0)

    def test_no_integers_returns_zero(self):
        self.assertEqual(sum_integers_in_string("hello world"), 0)

    def test_spaces_only_returns_zero(self):
        self.assertEqual(sum_integers_in_string("     "), 0)
    # Negative nums test

    def test_negative_numbers(self):
        self.assertEqual(sum_integers_in_string("-3 and -7"), -10)

    def test_mixed_positive_and_negative(self):
        self.assertEqual(sum_integers_in_string("10 -3 5"), 3)

    def test_all_negative_result(self):
        self.assertEqual(sum_integers_in_string("-100 -200"), -3)

    # Typerrors test
    def test_raises_type_error_for_integer_input(self):
        with self.assertRaises(TypeError):
            sum_integers_in_string(123)

    def test_raises_type_error_for_none_input(self):
        with self.assertRaises(TypeError):
            sum_integers_in_string(None)

    def test_raises_type_error_for_list_input(self):
        with self.assertRaises(TypeError):
            sum_integers_in_string([1, 2, 3])
    def test_raises_type_error_for_float_input(self):
        with self.assertRaises(TypeError):
            sum_integers_in_string(3.14)


if __name__ == "__main__":
    unittest.main(verbosity=2)
    