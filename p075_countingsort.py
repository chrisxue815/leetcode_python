import unittest


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        counts = [0] * 3
        for num in nums:
            counts[num] += 1

        sum_ = 0
        for i in xrange(3):
            count = counts[i]
            nums[sum_: sum_ + count] = [i] * count
            sum_ += count


class Test(unittest.TestCase):
    def test(self):
        self._test([], [])
        self._test([0], [0])
        self._test([2, 0, 1], [0, 1, 2])
        self._test([1, 2, 0], [0, 1, 2])
        self._test([2, 1, 0, 1], [0, 1, 1, 2])

    def _test(self, nums, expected):
        Solution().sortColors(nums)
        self.assertEqual(expected, nums)


if __name__ == '__main__':
    unittest.main()
