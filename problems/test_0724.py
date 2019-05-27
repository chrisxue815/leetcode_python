import unittest


# O(n).
class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1

        hi_sum = sum(nums)
        lo_sum = 0
        for i, num in enumerate(nums):
            hi_sum -= num
            if lo_sum == hi_sum:
                return i
            lo_sum += num
        return -1


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 7, 3, 6, 5, 6], 3)
        self._test([1, 2, 3], -1)

    def _test(self, nums, expected):
        actual = Solution().pivotIndex(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
