import sys
import unittest


class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minint = -sys.maxsize - 1
        a = b = c = minint
        
        for num in nums:
            if num > a:
                a, b, c = num, a, b
            elif num == a:
                continue
            elif num > b:
                b, c = num, b
            elif num == b:
                continue
            elif num > c:
                c = num

        if c != minint:
            return c
        return a


class Test(unittest.TestCase):
    def test(self):
        self._test([3, 2, 1], 1)
        self._test([2, 1], 2)
        self._test([2, 2, 3, 1], 1)

    def _test(self, nums, expected):
        actual = Solution().thirdMax(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
