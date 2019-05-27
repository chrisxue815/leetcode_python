import unittest


class Solution:
    def __init__(self):
        self.num = 0
        self.result = []

    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        self._backtrack(n)
        return self.result

    def _backtrack(self, n):
        if n == 0:
            self.result.append(self.num)
        else:
            n -= 1
            self._backtrack(n)
            self.num ^= 1 << n
            self._backtrack(n)


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
