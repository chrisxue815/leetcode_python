import unittest


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        result = 0x7FFFFFFF
        lo = 0
        sum_ = 0

        for hi in xrange(len(nums)):
            sum_ += nums[hi]
            if sum_ >= s:
                while lo < hi and sum_ - nums[lo] >= s:
                    sum_ -= nums[lo]
                    lo += 1
                if hi - lo < result:
                    result = hi - lo
        return result + 1 if result != 0x7FFFFFFF else 0


class Test(unittest.TestCase):
    def test(self):
        self._test(7, [2, 3, 1, 2, 4, 3], 2)

    def _test(self, s, nums, expected):
        actual = Solution().minSubArrayLen(s, nums)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
