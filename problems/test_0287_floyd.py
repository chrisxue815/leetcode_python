import unittest


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t = nums[0]
        h = nums[t]

        while t != h:
            t = nums[t]
            h = nums[nums[h]]

        t = 0
        while t != h:
            t = nums[t]
            h = nums[h]

        return t


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3, 4, 4, 5], 4)
        self._test([5, 1, 3, 4, 2, 4], 4)
        self._test([1, 2, 3, 4, 5, 5, 6], 5)
        self._test([1, 3, 4, 5, 6, 6, 6], 6)
        self._test([1, 3, 4, 5, 6, 6, 6, 7], 6)
        self._test([1, 3, 4, 2, 1], 1)

    def _test(self, nums, expected):
        actual = Solution().findDuplicate(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
