import unittest
from typing import Optional

import utils
from tree import TreeNode


def add_row(curr, val, depth):
    if not curr:
        return

    if depth > 2:
        add_row(curr.left, val, depth - 1)
        add_row(curr.right, val, depth - 1)
    else:
        child = TreeNode(val)
        child.left = curr.left
        curr.left = child
        child = TreeNode(val)
        child.right = curr.right
        curr.right = child


# O(n) time. O(log(n)) space. Recursive DFS.
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            node = TreeNode(val)
            node.left = root
            return node

        add_row(root, val, depth)
        return root


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, process_args=TreeNode.from_root_array, process_result=TreeNode.to_array_static)


if __name__ == '__main__':
    unittest.main()
