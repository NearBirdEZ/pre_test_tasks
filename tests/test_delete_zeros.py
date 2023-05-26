import unittest

from main import remove_zeros_for, remove_zeros_while


class TestDifferent(unittest.TestCase):
    def test_1_remove_zeros_for_fill(self) -> None:
        array: list[int] = [0, 1, 2, 0, 0, 0, 3, 4, 1, 2, 4, 6, -1, 56, 0, 8, 4]
        self.assertEqual(remove_zeros_for(array), [1, 2, 3, 4, 1, 2, 4, 6, -1, 56, 8, 4])

    def test_2_remove_zeros_for_while(self) -> None:
        array: list[int] = [0, 1, 2, 0, 0, 0, 3, 4, 1, 2, 4, 6, -1, 56, 0, 8, 4]
        self.assertEqual(remove_zeros_while(array), [1, 2, 3, 4, 1, 2, 4, 6, -1, 56, 8, 4])

    def test_3_remove_zeros_for_empty(self) -> None:
        array: list[int] = []
        self.assertEqual(remove_zeros_for(array), [])

    def test_4_remove_zeros_while_empty(self) -> None:
        array: list[int] = []
        self.assertEqual(remove_zeros_while(array), [])

    def test_5_remove_zeros_for_only_zeros(self) -> None:
        array: list[int] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(remove_zeros_for(array), [])

    def test_6_remove_zeros_while_only_zeros(self) -> None:
        array: list[int] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(remove_zeros_while(array), [])


if __name__ == '__main__':
    unittest.main()
