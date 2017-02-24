import unittest
from tree import TreeNode, null


class Solution(object):

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        vals = []
        stack = []
        cur = root

        while cur != None or len(stack) > 0:
            while cur != None:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            vals.append(cur.val)

            cur = cur.right

        return vals


class Test(unittest.TestCase):

    def test(self):
        root = TreeNode.from_array([1, null, 2, 3])
        self.assertEqual(
            Solution().inorderTraversal(root),
            [1, 3, 2])


if __name__ == '__main__':
    unittest.main()
