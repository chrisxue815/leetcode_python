import unittest


class Solution(object):
    def __init__(self):
        self.nums = None
        self.n = 0
        self.permutations = []
        self.result = []

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.nums = nums
        self.n = len(nums)
        self._permute()
        return self.result

    def _permute(self):
        if len(self.permutations) == self.n:
            self.result.append(list(self.permutations))
        else:
            for i in range(self.n):
                if self.nums[i] in self.permutations:
                    continue
                self.permutations.append(self.nums[i])
                self._permute()
                self.permutations.pop()


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3], [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1]
        ])

    def _test(self, nums, expected):
        actual = Solution().permute(nums)
        self.assertCountEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
