import unittest

from lab22 import find_sum


class TestFindTripletSum(unittest.TestCase):

    def test_example_1(self):
        arr = [1, 2, 3, 6]
        P = 6
        self.assertTrue(find_sum(arr, P))

if __name__ == "__main__":
    unittest.main()
