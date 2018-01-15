import unittest


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo = 1
        while lo < len(nums) and nums[lo - 1] <= nums[lo]:
            lo += 1
        if lo == len(nums):
            return 0
        lo -= 1

        hi = len(nums) - 2
        while nums[hi] <= nums[hi + 1]:
            hi -= 1
        hi += 1

        min_, max_ = nums[hi], nums[lo]

        for num in nums[lo + 1:hi]:
            if num < min_:
                min_ = num
            elif num > max_:
                max_ = num

        while lo >= 0 and nums[lo] > min_:
            lo -= 1
        while hi < len(nums) and nums[hi] < max_:
            hi += 1

        return hi - lo - 1


class Test(unittest.TestCase):
    def test(self):
        self._test([2, 6, 4, 8, 10, 9, 15], 5)

    def _test(self, nums, expected):
        actual = Solution().findUnsortedSubarray(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
