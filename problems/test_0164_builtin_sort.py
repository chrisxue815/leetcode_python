import unittest


# O(nlog(n)) time. Built-in sort (Timsort).
class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        gap = 0
        for i in range(len(nums) - 1):
            gap = max(gap, nums[i + 1] - nums[i])

        return gap


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3, 5, 6, 7, 0], 2)
        self._test([0, 1], 1)
        self._test([1, 1], 0)

    def _test(self, nums, expected):
        actual = Solution().maximumGap(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
