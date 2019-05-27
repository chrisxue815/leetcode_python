import unittest


class Solution:
    def __init__(self):
        self.nums = None
        self.n = 0
        self.combination = []
        self.result = [[]]

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        self.nums = nums
        self.n = len(nums)

        self._subsets(0)

        return self.result

    def _subsets(self, start):
        for i in range(start, self.n):
            if i > start and self.nums[i] == self.nums[i - 1]:
                continue
            self.combination.append(self.nums[i])
            self.result.append(list(self.combination))
            self._subsets(i + 1)
            self.combination.pop()


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 2], [
            [2],
            [1],
            [1, 2, 2],
            [2, 2],
            [1, 2],
            []
        ])

    def _test(self, nums, expected):
        actual = Solution().subsetsWithDup(nums)
        self.assertCountEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
