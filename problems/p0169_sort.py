import unittest


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[len(nums) >> 1]


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 2, 2], 2)
        self._test([-1], -1)

    def _test(self, nums, expected):
        actual = Solution().majorityElement(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
