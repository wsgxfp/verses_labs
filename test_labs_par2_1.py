import unittest
from labs_part2_1 import robots_way


class TestWayRobot(unittest.TestCase):

    def test_field_size_5x5(self):
        our_list = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20]]
        expected_result = [1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 11, 12, 13, 14, 15, 20, 19, 18, 17, 16]
        self.assertEqual(robots_way(our_list), expected_result)

    def test_field_size_2x4(self):
        our_list = [
            [1, 2, 3, 4],
            [5, 6, 7, 8]]
        expected_result = [1, 2, 3, 4, 8, 7, 6, 5]
        self.assertEqual(robots_way(our_list), expected_result)

    def test_field_size_1x6(self):
        our_list = [
            [1],
            [7],
            [11],
            [16],
            [1],
            [12]]
        expected_result = [1, 7, 11, 16, 1, 12]
        self.assertEqual(robots_way(our_list), expected_result)


if __name__ == '__main__':
    unittest.main()
