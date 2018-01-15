import unittest
import math


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and n == math.pow(3, round(math.log(n, 3)))


class Test(unittest.TestCase):
    def test(self):
        self._test(1, True)
        self._test(3, True)
        self._test(9, True)
        self._test(27, True)
        self._test(81, True)

        self._test(2, False)
        self._test(4, False)
        self._test(33, False)
        self._test(45, False)

        self._test(0, False)

    def _test(self, n, expected):
        actual = Solution().isPowerOfThree(n)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
