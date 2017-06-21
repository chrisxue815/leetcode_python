import unittest


class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10:
            return n

        num_digits = 2
        start = 10
        end = 190
        count = 90

        while n >= end:
            num_digits += 1
            count *= 10
            start = end
            end += count * num_digits

        n -= start
        r = n % num_digits

        if not r:
            return n // (num_digits * (10 ** (num_digits - 1))) + 1

        return n // num_digits % (10 ** (num_digits - r)) // (10 ** (num_digits - 1 - r))


class Test(unittest.TestCase):
    def test(self):
        self._test(1, 1)
        self._test(9, 9)
        self._test(10, 1)
        self._test(11, 0)
        self._test(20, 1)
        self._test(21, 5)
        self._test(30, 2)
        self._test(31, 0)
        self._test(32, 2)
        self._test(33, 1)
        self._test(188, 9)
        self._test(189, 9)
        self._test(190, 1)
        self._test(191, 0)
        self._test(192, 0)
        self._test(2887, 9)
        self._test(2888, 9)
        self._test(2889, 9)
        self._test(2890, 1)
        self._test(2891, 0)
        self._test(2892, 0)
        self._test(2893, 0)

    def _test(self, n, expected):
        actual = Solution().findNthDigit(n)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
