import unittest


class Solution:
    def __init__(self):
        self.nums = None
        self.n = 0
        self.result = []

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.nums = nums
        self.n = len(nums)
        self._permute(0)
        return self.result

    def _permute(self, start_index):
        nums = self.nums
        if start_index == self.n:
            self.result.append(list(nums))
        else:
            next_index = start_index + 1
            self._permute(next_index)

            for i in range(next_index, self.n):
                nums[i], nums[start_index] = nums[start_index], nums[i]
                self._permute(next_index)
                nums[i], nums[start_index] = nums[start_index], nums[i]


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
