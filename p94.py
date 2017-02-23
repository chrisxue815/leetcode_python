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
        stack.append(root)

        while len(stack) > 0:
            node = stack.pop()
            if node is None:
                continue
            if isinstance(node, TreeNode):
                stack.append(node.right)
                stack.append(node.val)
                stack.append(node.left)
            else:
                vals.append(node)

        return vals


class Test(unittest.TestCase):

    def test(self):
        root = TreeNode.from_array([1, null, 2, 3])
        self.assertEqual(
            Solution().inorderTraversal(root),
            [1, 3, 2])


if __name__ == '__main__':
    unittest.main()
