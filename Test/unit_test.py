#Unit Tests
import unittest
class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(1 + 1, 2)

# Run it with: python -m unittest unit_test.py in terminal