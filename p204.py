import unittest


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        is_composite = [False] * n
        count = 0
        for i in xrange(3, n, 2):
            if not is_composite[i]:
                count += 1
                for j in xrange(2, (n - 1) // i + 1):
                    is_composite[i * j] = True
        return count + 1


class Test(unittest.TestCase):
    def test(self):
        self._test(0, 0)
        self._test(1, 0)
        self._test(2, 0)
        self._test(3, 1)
        self._test(4, 2)
        self._test(5, 2)
        self._test(6, 3)
        self._test(7, 3)
        self._test(8, 4)

    def _test(self, n, expected):
        actual = Solution().countPrimes(n)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
