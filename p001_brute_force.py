import unittest


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, a in enumerate(nums):
            for j, b in enumerate(nums[i + 1:]):
                if a + b == target:
                    return [i, i + 1 + j]


class Test(unittest.TestCase):
    def test(self):
        self._test([2, 7, 11, 15], 9, [0, 1])
        self._test([11, 2, 7, 15], 9, [1, 2])
        self._test([2, 7, 11, 7, 15], 14, [1, 3])

    def _test(self, nums, target, expected):
        actual = Solution().twoSum(nums, target)
        self.assertItemsEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
