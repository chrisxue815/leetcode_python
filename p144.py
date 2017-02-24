import unittest
from tree import TreeNode, null


class Solution(object):

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        vals = []
        stack = []
        cur = root

        while cur != None or len(stack) > 0:
            while cur != None:
                vals.append(cur.val)
                stack.append(cur)
                cur = cur.left
            cur = stack.pop().right

        return vals


class Test(unittest.TestCase):

    def test(self):
        root = TreeNode.from_array([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(
            Solution().preorderTraversal(root),
            [1, 2, 4, 5, 3, 6, 7])


if __name__ == '__main__':
    unittest.main()
