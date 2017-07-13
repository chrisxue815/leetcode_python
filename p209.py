import unittest


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        result = len(nums)
        lo = 0
        sum_ = 0

        for hi in xrange(len(nums)):
            sum_ += nums[hi]
            if sum_ >= s:
                while sum_ >= s:
                    sum_ -= nums[lo]
                    lo += 1
                result = min(result, hi - lo)
        return result + 2 if result != len(nums) else 0


class Test(unittest.TestCase):
    def test(self):
        self._test(7, [2, 3, 1, 2, 4, 3], 2)

    def _test(self, s, nums, expected):
        actual = Solution().minSubArrayLen(s, nums)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
