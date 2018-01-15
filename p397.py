import unittest


class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n != 1:
            if not n & 1:
                n >>= 1
                count += 1
            elif n == 3 or n & 3 == 1:
                n >>= 1
                count += 2
            else:
                n += 1
                count += 1
        return count


class Test(unittest.TestCase):
    def test(self):
        self._test(8, 3)
        self._test(7, 4)
        self._test(15, 5)
        self._test(3, 2)
        self._test(100000000, 31)
        self._test(1234, 14)

    def _test(self, n, expected):
        actual = Solution().integerReplacement(n)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
