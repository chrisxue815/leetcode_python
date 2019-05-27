import unittest


class Solution:
    def __init__(self):
        self.end = 0
        self.combination = []
        self.result = []

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.end = n + 1
        self._combine(k, 1)
        return self.result

    def _combine(self, k, start):
        if k == 0:
            self.result.append(list(self.combination))
        elif start < self.end:
            # include
            self.combination.append(start)
            self._combine(k - 1, start + 1)
            self.combination.pop()

            # exclude
            self._combine(k, start + 1)


class Test(unittest.TestCase):
    def test(self):
        self._test(4, 2, [
            [2, 4],
            [3, 4],
            [2, 3],
            [1, 2],
            [1, 3],
            [1, 4],
        ])

    def _test(self, n, k, expected):
        actual = Solution().combine(n, k)
        self.assertCountEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
