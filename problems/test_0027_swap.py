import unittest


class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            if nums[lo] == val:
                nums[lo], nums[hi] = nums[hi], nums[lo]
                hi -= 1
            else:
                lo += 1
        return lo


class Test(unittest.TestCase):
    def test(self):
        self._test([3, 2, 2, 3], 3, [2, 2])

    def _test(self, nums, val, expected):
        actual = Solution().removeElement(nums, val)
        self.assertEqual(len(expected), actual)
        self.assertEqual(expected, nums[:actual])


if __name__ == '__main__':
    unittest.main()
