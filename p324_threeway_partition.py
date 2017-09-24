import unittest
import numpy


# O(n) time, O(1) space. Three-way partitioning, index mapping, math
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
        half = (len(nums) - 1) >> 1

        def map_index(i):
            return (half - i) << 1 if i <= half else ((n - i - 1) << 1) + 1

        while mid <= hi:
            vmid = map_index(mid)
            if nums[vmid] < median:
                vlo = map_index(lo)
                nums[vlo], nums[vmid] = nums[vmid], nums[vlo]
                lo += 1
                mid += 1
            elif nums[vmid] > median:
                vhi = map_index(hi)
                nums[vmid], nums[vhi] = nums[vhi], nums[vmid]
                hi -= 1
            else:
                mid += 1


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
