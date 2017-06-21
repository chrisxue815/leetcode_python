import unittest
import itertools


class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0
        n = len(A)
        sum_ = sum(A)
        f = sum(i * num for i, num in enumerate(A))
        max_ = f

        for num in itertools.islice(A, n - 1):
            f += n * num - sum_
            if f > max_:
                max_ = f
        return max_


class Test(unittest.TestCase):
    def test(self):
        self._test([4, 3, 2, 6], 26)

    def _test(self, A, expected):
        actual = Solution().maxRotateFunction(A)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
