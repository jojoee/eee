import unittest
from eee import e


class TestSum(unittest.TestCase):
    def test_e_default(self):
        self.assertEqual(e(), "eee", "Should be 'eee'")

    def test_e(self):
        self.assertEqual(e(5), "eeeee", "Should be 'eeeee'")


if __name__ == "__main__":
    unittest.main()
