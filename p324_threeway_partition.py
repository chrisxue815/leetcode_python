import unittest
import numpy


# O(n) time, O(n) space. Three-way partitioning, math
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        median = int(numpy.median(nums))
        n = len(nums)

        lo = mid = 0
        hi = n - 1

        while mid <= hi:
            if nums[mid] < median:
                nums[lo], nums[mid] = nums[mid], nums[lo]
                lo += 1
                mid += 1
            elif nums[mid] > median:
                nums[mid], nums[hi] = nums[hi], nums[mid]
                hi -= 1
            else:
                mid += 1

        half = (len(nums) + 1) >> 1
        nums[::2], nums[1::2] = reversed(nums[:half]), reversed(nums[half:])


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 3, 2, 2, 3, 1])
        self._test([1, 2, 1, 2, 1, 1, 2, 2, 1])
        self._test([1, 5, 1, 1, 6, 4])
        self._test([1, 2, 2, 3])

    def _test(self, nums):
        Solution().wiggleSort(nums)

        prev = nums[0] + 1
        asc = False
        for num in nums:
            if asc:
                self.assertLess(prev, num)
            else:
                self.assertGreater(prev, num)
            prev = num
            asc = not asc


if __name__ == '__main__':
    unittest.main()
