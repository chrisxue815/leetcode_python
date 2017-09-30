import unittest


# O(1). Bit manipulation.
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        prev = n & 1
        n >>= 1
        while n:
            if n & 1 == prev:
                return False
            prev = not prev
            n >>= 1
        return True


class Test(unittest.TestCase):
    def test(self):
        self._test(5, True)
        self._test(6, False)
        self._test(7, False)
        self._test(10, True)
        self._test(11, False)

    def _test(self, n, expected):
        actual = Solution().hasAlternatingBits(n)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
