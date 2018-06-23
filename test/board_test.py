import unittest
from game.board import Board

class BoardTestBase(unittest.TestCase):
    def setUp(self):
        self.size = 20
        self.board = Board(self.size)
        for x in range(self.size):
            for y in range(self.size):
                self.board.set_element(x, y, x * 100 + y)

class BoardTest_GetElement(BoardTestBase):
    def test_get_element_returns_the_expected_value(self):
        x = 5
        y = 10
        self.assertEqual(510, self.board.get_element(x, y))

    def test_get_element_throws_expection_if_x_is_too_big(self):
        self.assertRaises(IndexError, self.board.get_element, 100, 0)

    def test_get_element_throws_expection_if_y_is_too_big(self):
        self.assertRaises(IndexError, self.board.get_element, 0, 100)

    def test_get_element_throws_expection_if_x_is_negative(self):
        self.assertRaises(IndexError, self.board.get_element, -1, 0)

    def test_get_element_throws_expection_if_y_is_negative(self):
        self.assertRaises(IndexError, self.board.get_element, 0, -1)

class BoardTest_GetElementArray(BoardTestBase):
    def do_test(self, dir, expectation):
        x = 5
        y = 10
        n = 3
        self.assertEqual(expectation, self.board.get_element_array(x, y, n, dir))

    def test_get_element_array_returns_the_expected_array_with_dir_0(self):
        self.do_test(0, [510, 511, 512])

    def test_get_element_array_returns_the_expected_array_with_dir_1(self):
        self.do_test(1, [510, 411, 312])

    def test_get_element_array_returns_the_expected_array_with_dir_2(self):
        self.do_test(2, [510, 410, 310])

    def test_get_element_array_returns_the_expected_array_with_dir_3(self):
        self.do_test(3, [510, 409, 308])

    def test_get_element_array_returns_the_expected_array_with_dir_4(self):
        self.do_test(4, [510, 509, 508])

    def test_get_element_array_returns_the_expected_array_with_dir_5(self):
        self.do_test(5, [510, 609, 708])

    def test_get_element_array_returns_the_expected_array_with_dir_6(self):
        self.do_test(6, [510, 610, 710])

    def test_get_element_array_returns_the_expected_array_with_dir_7(self):
        self.do_test(7, [510, 611, 712])

    def test_get_element_array_throws_expection_by_out_of_range(self):
        self.assertRaises(IndexError, self.board.get_element_array, 5, 10, 100, 0)

    def test_get_element_array_throws_expection_by_negative_index(self):
        self.assertRaises(IndexError, self.board.get_element_array, -1, 10, 10, 0)

if __name__ == '__main__':
    unittest.main()