import unittest


# O(n), three-way partitioning
# https://en.wikipedia.org/wiki/Dutch_national_flag_problem
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        n = len(nums)

        lo = mid = 0
        hi = n - 1

        while mid <= hi:
            if nums[mid] == 0:
                nums[lo], nums[mid] = nums[mid], nums[lo]
                lo += 1
                mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[hi] = nums[hi], nums[mid]
                hi -= 1
            else:
                mid += 1


class Test(unittest.TestCase):
    def test(self):
        self._test([], [])
        self._test([0], [0])
        self._test([2, 0, 1], [0, 1, 2])
        self._test([2, 0], [0, 2])
        self._test([1, 2, 0, 0], [0, 0, 1, 2])
        self._test([1, 2, 0], [0, 1, 2])
        self._test([2, 1, 0, 1], [0, 1, 1, 2])

    def _test(self, nums, expected):
        Solution().sortColors(nums)
        self.assertEqual(expected, nums)


if __name__ == '__main__':
    unittest.main()
