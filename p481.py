import unittest
import itertools


class Solution(object):
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
        s = [0] * n
        s[0] = 1
        s[1] = 2
        s[2] = 2
        w = 3
        next_ = 1

        for r in itertools.islice(s, 2, len(s)):
            for _ in xrange(r):
                s[w] = next_
                if next_ == 1:
                    result += 1
                w += 1
                if w == n:
                    return result
            next_ = 2 if next_ == 1 else 1


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
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
