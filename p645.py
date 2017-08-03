import unittest


class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        s = sum(set(nums))
        return [sum(nums) - s, ((1 + n) * n >> 1) - s]


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 2, 4], [2, 3])

    def _test(self, nums, expected):
        actual = Solution().findErrorNums(nums)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
