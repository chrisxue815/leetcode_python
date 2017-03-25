import sys
import unittest


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        if len(nums) == 1:
            return 0

        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = lo + ((hi - lo) >> 1)
            mid_val = nums[mid]
            right = nums[mid + 1]

            if mid_val < right:
                lo = mid + 1
            else:
                left = nums[mid - 1] if mid >= 1 else -sys.maxint - 1
                if mid_val > left:
                    return mid
                else:
                    hi = mid - 1
        return lo


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3, 1], 2)

    def _test(self, nums, expected):
        actual = Solution().findPeakElement(nums)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
