import unittest


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        lo = 0
        hi = n

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                return mid

        if lo < n and nums[lo] < target:
            lo += 1

        return lo


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 3, 5, 6], 5, 2)
        self._test([1, 3, 5, 6], 2, 1)
        self._test([1, 3, 5, 6], 7, 4)
        self._test([1, 3, 5, 6], 0, 0)

    def _test(self, nums, target, expected):
        actual = Solution().searchInsert(nums, target)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
