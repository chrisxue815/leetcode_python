import unittest


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        n = len(nums)

        k %= n
        if k == 0:
            return
        if k < 0:
            k += n

        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4])
        self._test([1, 2, 3, 4, 5, 6, 7], 10, [5, 6, 7, 1, 2, 3, 4])
        self._test([1, 2, 3, 4, 5, 6, 7], -4, [5, 6, 7, 1, 2, 3, 4])
        self._test([1, 2, 3, 4, 5, 6, 7], 4, [4, 5, 6, 7, 1, 2, 3])

    def _test(self, nums, k, expected):
        Solution().rotate(nums, k)
        self.assertEqual(nums, expected)


if __name__ == '__main__':
    unittest.main()
