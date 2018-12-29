import unittest
from tree import TreeNode


# O(n). Recursive post-order DFS.
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.result = 0
        self._dfs(root)
        return self.result

    def _dfs(self, root):
        if not root:
            return 0

        left = self._dfs(root.left)
        right = self._dfs(root.right)

        result = 0

        if root.left and root.left.val == root.val:
            left += 1
            result = left
        else:
            left = 0

        if root.right and root.right.val == root.val:
            right += 1
            result += right
        else:
            right = 0

        if result > self.result:
            self.result = result

        return max(left, right)


class Test(unittest.TestCase):
    def test(self):
        self._test([5, 4, 5, 1, 1, None, 5], 2)
        self._test([1, 4, 5, 4, 4, None, 5], 2)

    def _test(self, root, expected):
        root = TreeNode.from_array(root)
        actual = Solution().longestUnivaluePath(root)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
