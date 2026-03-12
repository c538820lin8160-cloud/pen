import unittest

from pen.main import add


class TestMain(unittest.TestCase):
    def test_add_positive_numbers(self) -> None:
        self.assertEqual(add(1, 2), 3)

    def test_add_with_zero(self) -> None:
        self.assertEqual(add(0, 5), 5)


if __name__ == "__main__":
    unittest.main()
