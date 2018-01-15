import unittest


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            lo_val = nums[lo]
            if lo_val <= nums[hi]:
                return lo_val

            mid = lo + ((hi - lo) >> 1)
            mid_val = nums[mid]

            if mid_val < lo_val:
                hi = mid
            else:
                lo = mid + 1

        return nums[lo]


class Test(unittest.TestCase):
    def test(self):
        self._test([4, 5, 6, 7, 0, 1, 2], 0)
        self._test([0, 1, 2, 4, 5, 6, 7], 0)

    def _test(self, nums, expected):
        actual = Solution().findMin(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
