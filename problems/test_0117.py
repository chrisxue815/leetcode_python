import unittest

from tree_link_node import Node


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
        phantom = Node(0)
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

            curr = curr.next

            if not curr:
                if not phantom.next:
                    break
                prev = phantom
                curr = phantom.next
                phantom.next = None


class Test(unittest.TestCase):

    def test(self):
        self._test([4, 2, 6, 1, 3, 5, 7], [4, None, 2, 6, None, 1, 3, 5, 7, None])

    def _test(self, vals, expected):
        root = Node.from_array(vals)
        Solution().connect(root)
        self.assertEqual(expected, Node.to_next_value_array(root))


if __name__ == '__main__':
    unittest.main()
