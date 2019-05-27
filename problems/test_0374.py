import unittest

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
_my_num = 0


def guess(num):
    if _my_num < num:
        return -1
    elif _my_num > num:
        return 1
    return 0


class Solution:
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo = 1
        hi = n
        while True:
            mid = lo + (hi - lo) // 2
            result = guess(mid)
            if result == -1:
                hi = mid - 1
            elif result == 1:
                lo = mid + 1
            else:
                return mid


class Test(unittest.TestCase):
    def test(self):
        self._test(10, 6)

    def _test(self, n, expected):
        global _my_num
        _my_num = expected
        actual = Solution().guessNumber(n)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
