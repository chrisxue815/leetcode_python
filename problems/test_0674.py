import unittest


# O(n)
class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        result = 1
        lo = 0
        prev = nums[0]
        for hi, curr in enumerate(nums):
            if prev >= curr:
                result = max(result, hi - lo)
                lo = hi
            prev = curr
        return max(result, len(nums) - lo)


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 3, 5, 4, 7], 3)
        self._test([1, 3, 5, 6, 7], 5)
        self._test([2, 2, 2, 2, 2], 1)

    def _test(self, nums, expected):
        actual = Solution().findLengthOfLCIS(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
