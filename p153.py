import unittest


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pivot = nums[0]
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = lo + ((hi - lo) >> 1)
            mid_val = nums[mid]
            if mid_val < pivot:
                hi = mid - 1
            else:
                lo = mid + 1

        if lo == len(nums):
            return pivot
        return nums[lo]


class Test(unittest.TestCase):
    def test(self):
        self._test([4, 5, 6, 7, 0, 1, 2], 0)
        self._test([0, 1, 2, 4, 5, 6, 7], 0)

    def _test(self, nums, expected):
        actual = Solution().findMin(nums)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
