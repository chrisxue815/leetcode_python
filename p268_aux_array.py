import unittest


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        visited = [0] * (n + 1)
        for num in nums:
            visited[num] = 1
        for i, num in enumerate(visited):
            if num == 0:
                return i


class Test(unittest.TestCase):
    def test(self):
        self._test([0, 1, 3], 2)
        self._test([0, 1, 2], 3)

    def _test(self, nums, expected):
        actual = Solution().missingNumber(nums)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
