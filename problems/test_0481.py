import unittest
import itertools


class Solution:
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        if n <= 3:
            return 1

        result = 1
        s = [0] * (n + 1)
        s[0] = 1
        s[1] = 2
        s[2] = 2
        w = 3
        next_ = 1

        for r in itertools.islice(s, 2, len(s)):
            for _ in range(r):
                s[w] = next_
                w += 1
            if next_ == 1:
                result += r
            if w >= n:
                return result - 1 if w == n + 1 and s[n] == 1 else result
            next_ = 3 - next_


class Test(unittest.TestCase):
    def test(self):
        self._test(1, 1)
        self._test(2, 1)
        self._test(3, 1)
        self._test(4, 2)
        self._test(5, 3)
        self._test(6, 3)

    def _test(self, n, expected):
        actual = Solution().magicalString(n)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
