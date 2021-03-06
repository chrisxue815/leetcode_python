import unittest
from tree import TreeLinkNode, null

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing

    def connect(self, root):
        if not root:
            return

        curr = root
        next_level = curr.left

        while next_level:
            while curr:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                curr = curr.next
            curr = next_level
            next_level = curr.left


class Test(unittest.TestCase):

    def test(self):
        self._test([4, 2, 6, 1, 3, 5, 7])

    def _test(self, vals):
        root = TreeLinkNode.from_array(vals)
        Solution().connect(root)
        self.assertEqual(vals, root.to_array_bfs_fulltree())


if __name__ == '__main__':
    unittest.main()
