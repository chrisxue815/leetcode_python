import unittest


class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo = 0
        hi = (len(nums) >> 1) - 1
        while lo <= hi:
            mid = lo + ((hi - lo) >> 1)
            if nums[mid << 1] == nums[(mid << 1) + 1]:
                lo = mid + 1
            else:
                hi = mid - 1
        return nums[lo << 1]


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 1, 2, 3, 3, 4, 4, 8, 8], 2)
        self._test([3, 3, 7, 7, 10, 11, 11], 10)
        self._test([1, 1, 2], 2)
        self._test([1, 2, 2], 1)
        self._test([1], 1)

    def _test(self, nums, expected):
        actual = Solution().singleNonDuplicate(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
