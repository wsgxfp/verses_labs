import unittest

from lab2 import find_sum


class TestFindSum(unittest.TestCase):
    def test_existence(self):
        M = [100, 225, 356, 4221, 625, 906, 1437, 821, 950, 1000]
        P = 681
        self.assertTrue(find_sum(M, P))

    def test_nonexistence(self):
        M =[100, 225, 356, 4221, 625, 906, 1437, 821, 950, 1000]
        P = 100
        self.assertFalse(find_sum(M, P))

    def test_specific_elements(self):
        M = [100, 225, 356, 4221, 625, 906, 1437, 821, 950, 1000]
        P = 1675
        self.assertTrue(find_sum(M, P))

    def test_another_combination(self):
        M = [100, 225, 356, 4221, 625, 906, 1437, 821, 950, 1000]
        P = 2131
        self.assertTrue(find_sum(M, P))


if __name__ == '__main__':
    unittest.main()
