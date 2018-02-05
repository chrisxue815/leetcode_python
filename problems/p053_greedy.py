import unittest


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        max_sum = nums[0]
        cur_sum = max_sum

        for num in nums[1:]:
            if cur_sum <= 0:
                cur_sum = num
            else:
                cur_sum += num

            if cur_sum > max_sum:
                max_sum = cur_sum

        return max_sum


class Test(unittest.TestCase):
    def test(self):
        self._test([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6)
        self._test([-2, -1], -1)

    def _test(self, nums, expected):
        actual = Solution().maxSubArray(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()