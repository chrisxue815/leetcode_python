import unittest
from tree import TreeNode, null

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class BSTIterator:

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        stack = []
        self.stack = stack
        while root:
            stack.append(root)
            root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0

    def next(self):
        """
        :rtype: int
        """
        stack = self.stack

        if not stack:
            return None

        curr = stack.pop()
        nextnode = curr.right

        while nextnode:
            stack.append(nextnode)
            nextnode = nextnode.left

        return curr.val


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())


class Test(unittest.TestCase):

    def test(self):
        self._test([4, 2, 6, 1, 3, 5, 7])

    def _test(self, vals):
        root = TreeNode.from_array(vals)
        i, v = BSTIterator(root), []
        while i.hasNext():
            v.append(i.next())
        self.assertEqual(root.to_array_inorder(), v)


if __name__ == '__main__':
    unittest.main()
