import unittest


class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return [i ^ (i >> 1) for i in range(1 << n)]


class Test(unittest.TestCase):
    def test(self):
        self._test(0, [0])
        self._test(1, [0, 1])
        self._test(2, [0, 1, 3, 2])

    def _test(self, n, expected):
        actual = Solution().grayCode(n)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
