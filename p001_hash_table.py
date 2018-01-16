import unittest


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_to_index = {}

        for i, num in enumerate(nums):
            if target - num in num_to_index:
                return [num_to_index[target - num], i]
            num_to_index[num] = i


class Test(unittest.TestCase):
    def test(self):
        self._test([2, 7, 11, 15], 9, [0, 1])
        self._test([11, 2, 7, 15], 9, [1, 2])
        self._test([2, 7, 11, 7, 15], 14, [1, 3])

    def _test(self, nums, target, expected):
        actual = Solution().twoSum(nums, target)
        self.assertItemsEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
