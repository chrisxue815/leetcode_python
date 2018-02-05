import unittest
from tree import TreeNode


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        vals = []
        stack = []
        cur = root

        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                vals.append(cur.val)
                cur = cur.right

        return vals


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3, 4, 5, 6, 7], [4, 2, 5, 1, 6, 3, 7])

    def _test(self, root, expected):
        root = TreeNode.from_array(root)
        actual = Solution().inorderTraversal(root)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()