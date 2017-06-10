import unittest


class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        types = set(candies)
        half = len(candies) // 2
        return len(types) if len(types) < half else half


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 1, 2, 2, 3, 3], 3)
        self._test([1, 1, 2, 3], 2)

    def _test(self, candies, expected):
        actual = Solution().distributeCandies(candies)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
