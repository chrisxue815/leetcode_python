import unittest


class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = set()
        stack = []

        def dfs(i):
            for i in xrange(i, len(nums)):
                if not stack or nums[i] >= stack[-1]:
                    stack.append(nums[i])
                    if len(stack) > 1:
                        result.add(tuple(stack))
                    dfs(i + 1)
                    stack.pop()

        dfs(0)

        return [list(item) for item in result]


class Test(unittest.TestCase):
    def test(self):
        self._test(
            [4, 6, 7, 7],
            [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7, 7], [4, 7, 7]]
        )

    def _test(self, nums, expected):
        actual = Solution().findSubsequences(nums)
        self.assertItemsEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
