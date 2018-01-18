import unittest
from tree import TreeNode


class Solution(object):
    def postorderTraversal(self, root):
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
                cur = cur.right
            else:
                cur = stack.pop()
                cur = cur.left

        vals.reverse()
        return vals


class Test(unittest.TestCase):
    def test(self):
        root = TreeNode.from_array([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual([4, 5, 2, 6, 7, 3, 1], Solution().postorderTraversal(root))


if __name__ == '__main__':
    unittest.main()
