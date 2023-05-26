import unittest

from main import find_different_elements


class TestDifferent(unittest.TestCase):
    def test_1_find_different_elements_fill(self) -> None:
        array1: list[int] = [1, 2, 3]
        array2: list[int] = [3, 4, 5]
        answer: set[int] = {1, 2}
        self.assertEqual(find_different_elements(array1, array2), answer)

    def test_2_find_different_elements_empty(self) -> None:
        array1: list[int] = []
        array2: list[int] = []
        answer: set[int] = set()
        self.assertEqual(find_different_elements(array1, array2), answer)

    def test_3_find_different_elements_first_empty(self) -> None:
        array1: list[int] = []
        array2: list[int] = [3, 4, 5]
        answer: set[int] = set()
        self.assertEqual(find_different_elements(array1, array2), answer)

    def test_4_find_different_elements_second_empty(self) -> None:
        array1: list[int] = [1, 2, 3]
        array2: list[int] = []
        answer: set[int] = {1, 2, 3}
        self.assertEqual(find_different_elements(array1, array2), answer)


if __name__ == '__main__':
    unittest.main()
