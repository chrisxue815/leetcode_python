import unittest


# O(n). Induction, binary search
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in xrange(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                break
        else:
            i = -1

        nums[i + 1:] = nums[i + 1:][::-1]

        if i == -1:
            return

        target = nums[i]
        lo = i + 1
        hi = len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) >> 1
            mid_val = nums[mid]
            if mid_val <= target:
                lo = mid + 1
            else:
                hi = mid - 1

        nums[i], nums[lo] = nums[lo], nums[i]


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3], [1, 3, 2])
        self._test([3, 2, 1], [1, 2, 3])
        self._test([1, 1, 5], [1, 5, 1])

    def _test(self, nums, expected):
        Solution().nextPermutation(nums)
        self.assertEqual(expected, nums)


if __name__ == '__main__':
    unittest.main()
