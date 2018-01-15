import unittest


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        lo = 0
        hi = n - 1

        while lo <= hi:
            mid = lo + ((hi - lo) >> 1)
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                return mid

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
