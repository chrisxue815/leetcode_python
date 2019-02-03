import unittest


class Solution(object):
    def __init__(self):
        self.nums = None
        self.n = 0
        self.combination = []
        self.result = [[]]

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.nums = nums
        self.n = len(nums)

        self._subsets(0)

        return self.result

    def _subsets(self, start):
        for i in range(start, self.n):
            self.combination.append(self.nums[i])
            self.result.append(list(self.combination))
            self._subsets(i + 1)
            self.combination.pop()


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3], [
            [3],
            [1],
            [2],
            [1, 2, 3],
            [1, 3],
            [2, 3],
            [1, 2],
            []
        ])

    def _test(self, nums, expected):
        actual = Solution().subsets(nums)
        self.assertCountEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
