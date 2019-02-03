import unittest
from tree import TreeLinkNode, null


# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None


class Solution(object):
    # @param root, a tree link node
    # @return nothing

    def connect(self, root):
        if not root:
            return

        curr = root
        phantom = TreeLinkNode(0)
        prev = phantom

        while True:
            if curr.left:
                prev.next = curr.left
                if curr.right:
                    curr.left.next = curr.right
                    prev = curr.right
                else:
                    prev = curr.left
            elif curr.right:
                prev.next = curr.right
                prev = curr.right

            curr = curr.__next__

            if not curr:
                if not phantom.__next__:
                    break
                prev = phantom
                curr = phantom.__next__
                phantom.next = None


class Test(unittest.TestCase):

    def test(self):
        self._test([4, 2, 6, 1, 3, 5, 7])

    def _test(self, vals):
        root = TreeLinkNode.from_array(vals)
        Solution().connect(root)
        self.assertEqual(vals, root.to_array_bfs_fulltree())


if __name__ == '__main__':
    unittest.main()
