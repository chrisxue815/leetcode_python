import unittest
from tree import TreeNode


class Solution(object):
    def preorderTraversal(self, root):
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
                vals.append(cur.val)
                cur = cur.left
            else:
                cur = stack.pop()
                cur = cur.right

        return vals


class Test(unittest.TestCase):
    def test(self):
        root = TreeNode.from_array([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual([1, 2, 4, 5, 3, 6, 7], Solution().preorderTraversal(root))


if __name__ == '__main__':
    unittest.main()
