import unittest
import sys


class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        indices = {}
        for index1, rest in enumerate(list1):
            indices[rest] = index1
        common = []
        min_sum = sys.maxint
        for index2, rest in enumerate(list2):
            index1 = indices.get(rest, -1)
            if index1 != -1:
                index_sum = index1 + index2
                if index_sum < min_sum:
                    min_sum = index_sum
                    common = [rest]
                elif index_sum == min_sum:
                    common.append(rest)
        return common


class Test(unittest.TestCase):
    def test(self):
        self._test(
            ['Shogun', 'Tapioca Express', 'Burger King', 'KFC'],
            ['Piatti', 'The Grill at Torrey Pines', 'Hungry Hunter Steakhouse', 'Shogun'],
            ['Shogun'])
        self._test(
            ['Shogun', 'Tapioca Express', 'Burger King', 'KFC'],
            ['KFC', 'Shogun', 'Burger King'],
            ['Shogun'])

    def _test(self, list1, list2, expected):
        actual = Solution().findRestaurant(list1, list2)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
