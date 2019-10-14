import unittest
from eee import e


class TestSum(unittest.TestCase):
    def test_e(self):
        self.assertEqual(e(3), "eee", "Should be 'eee'")


if __name__ == "__main__":
    unittest.main()
