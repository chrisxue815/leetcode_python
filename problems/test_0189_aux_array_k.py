import unittest


class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        if k < 0:
            k += n
        m = n - k
        if k < m:
            aux = nums[m:]
            nums[k:] = nums[:m]
            nums[:k] = aux
        else:
            aux = nums[:m]
            nums[:k] = nums[m:]
            nums[k:] = aux


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4])
        self._test([1, 2, 3, 4, 5, 6, 7], 10, [5, 6, 7, 1, 2, 3, 4])
        self._test([1, 2, 3, 4, 5, 6, 7], -4, [5, 6, 7, 1, 2, 3, 4])
        self._test([1, 2, 3, 4, 5, 6, 7], 4, [4, 5, 6, 7, 1, 2, 3])

    def _test(self, nums, k, expected):
        Solution().rotate(nums, k)
        self.assertEqual(expected, nums)


if __name__ == '__main__':
    unittest.main()
