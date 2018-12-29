import unittest


# O(n) time. O(n) space. Partitioning, left and right max.
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or not k:
            return []

        result = [0] * (len(nums) - k + 1)
        left_max = [0] * len(nums)
        right_max = [0] * len(nums)
        curr_max = -0x80000000

        for i, num in enumerate(nums):
            if curr_max < num or i % k == 0:
                curr_max = num
            left_max[i] = curr_max

        for i in xrange(len(nums) - 1, -1, -1):
            num = nums[i]
            if curr_max < num or i % k == k - 1:
                curr_max = num
            right_max[i] = curr_max

        for i in xrange(len(result)):
            result[i] = max(right_max[i], left_max[i + k - 1])

        return result


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7])

    def _test(self, nums, k, expected):
        actual = Solution().maxSlidingWindow(nums, k)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
