import unittest


class Solution(object):
    def __init__(self):
        self.result = []

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if k <= 0 or n <= 0:
            return []

        self._combine([], k, 1, n)

        return self.result

    def _combine(self, combination, k, start, n):
        if k == 1:
            if start <= n <= 9:
                self.result.append(combination + [n])
        else:
            end = min(10, n)
            for i in xrange(start, end):
                combination.append(i)
                self._combine(combination, k - 1, i + 1, n - i)
                combination.pop()


class Test(unittest.TestCase):
    def test(self):
        self._test(3, 7, [[1, 2, 4]])
        self._test(3, 9, [[1, 2, 6], [1, 3, 5], [2, 3, 4]])

    def _test(self, k, n, expected):
        actual = Solution().combinationSum3(k, n)
        self.assertItemsEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
