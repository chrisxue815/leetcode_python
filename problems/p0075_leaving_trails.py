import unittest


# O(n), leaving trails
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        lo = mid = 0

        for hi in xrange(len(nums)):
            num = nums[hi]
            nums[hi] = 2
            if num < 2:
                nums[mid] = 1
                mid += 1
            if num == 0:
                nums[lo] = 0
                lo += 1


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
