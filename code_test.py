import unittest
from example_code import reverse_array, get_secrets

class TestExampleCode(unittest.TestCase):

    def test_reverse_array(self):
        self.assertEqual(reverse_array([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])
        self.assertEqual(reverse_array([]), [])
        self.assertEqual(reverse_array([1]), [1])

    def test_get_secrets(self):
        # Assuming the .env file or environment has the correct SECRET_KEY set
        expected_secret = 'secret'
        actual_secret = get_secrets()
        self.assertEqual(actual_secret, expected_secret, f"Expected {expected_secret}, but got {actual_secret}")

if __name__ == '__main__':
    unittest.main()
