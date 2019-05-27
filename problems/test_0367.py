import unittest


class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        lo = 0
        hi = num

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            midsq = mid * mid
            if midsq > num:
                hi = mid - 1
            elif midsq < num:
                lo = mid + 1
            else:
                return True

        return False


class Test(unittest.TestCase):
    def test(self):
        self._test(16, True)
        self._test(14, False)

    def _test(self, num, expected):
        actual = Solution().isPerfectSquare(num)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
