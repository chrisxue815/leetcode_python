import unittest


class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo = 1
        hi = n
        step = 1
        lr = True

        while lo < hi:
            if lr:
                if ((hi - lo) // step) & 1 == 0:
                    hi -= step
                lo += step
            else:
                if ((hi - lo) // step) & 1 == 0:
                    lo += step
                hi -= step
            step *= 2
            lr = not lr

        return lo


class Test(unittest.TestCase):
    def test(self):
        self._test(1, 1)
        self._test(2, 2)
        self._test(3, 2)
        self._test(4, 2)
        self._test(5, 2)
        self._test(6, 4)
        self._test(7, 4)
        self._test(8, 6)
        self._test(9, 6)
        self._test(10, 8)
        self._test(11, 8)
        self._test(12, 6)
        self._test(13, 6)

    def _test(self, n, expected):
        actual = Solution().lastRemaining(n)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
