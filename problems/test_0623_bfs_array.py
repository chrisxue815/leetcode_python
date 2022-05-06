import unittest
from typing import Optional

import utils
from tree import TreeNode


# O(n) time. O(n) space. BFS.
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            curr = TreeNode(val)
            curr.left = root
            return curr

        q = [root]
        for _ in range(depth - 2):
            q = [child for node in q for child in (node.left, node.right) if child]

        for curr in q:
            child = TreeNode(val)
            child.left = curr.left
            curr.left = child
            child = TreeNode(val)
            child.right = curr.right
            curr.right = child

        return root


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, process_args=TreeNode.from_root_array, process_result=TreeNode.to_array_static)


if __name__ == '__main__':
    unittest.main()
