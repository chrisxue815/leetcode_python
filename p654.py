import unittest
from tree import TreeNode


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        max_i, max_num = 0, nums[0]
        for i, num in enumerate(nums):
            if num > max_num:
                max_i, max_num = i, num
        root = TreeNode(max_num)
        root.left = self.constructMaximumBinaryTree(nums[:max_i])
        root.right = self.constructMaximumBinaryTree(nums[max_i + 1:])
        return root


class Test(unittest.TestCase):
    def test(self):
        self._test([3, 2, 1, 6, 0, 5], [6, 3, 5, None, 2, 0, None, None, 1])

    def _test(self, nums, expected):
        actual = Solution().constructMaximumBinaryTree(nums)
        actual = actual.to_array()
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
