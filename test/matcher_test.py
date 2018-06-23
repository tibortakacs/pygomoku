import unittest
from player.rulematcher.matcher import Matcher

class MatcherTest(unittest.TestCase):
    def test_returns_the_expected_index_if_the_rule_matches_on_the_row(self):
        matcher = Matcher(1, 2, 0)

        rule = "xxoXxx"
        row = [1, 1, 2, 0, 1, 1]

        self.assertEqual(3, matcher.match(rule, row))

    def test_returns_the_expected_index_if_the_rule_matches_on_the_row_using_different_values(self):
        matcher = Matcher(5, 7, 0)

        rule = "xxoXxx"
        row = [5, 5, 7, 0, 5, 5]

        self.assertEqual(3, matcher.match(rule, row))

    def test_return_minus_one_if_the_rule_and_the_row_have_different_sizes(self):
        matcher = Matcher(1, 2, 0)

        rule = "xx"
        row = [1, 1, 2, 0, 1, 1]

        self.assertEqual(-1, matcher.match(rule, row))

    def test_return_minus_one_if_the_rule_does_not_match_on_the_row(self):
        matcher = Matcher(1, 2, 0)

        rule = "xxxXxx"
        row = [1, 1, 2, 0, 1, 1]

        self.assertEqual(-1, matcher.match(rule, row))

    def test_return_minus_one_if_X_could_fit_into_different_places(self):
        matcher = Matcher(1, 2, 0)

        rule = "xxoXXx" # Invalid use case
        row = [1, 1, 2, 0, 0, 1]

        self.assertEqual(-1, matcher.match(rule, row))

if __name__ == '__main__':
    unittest.main()