import unittest

import utils
from tree import TreeNode


# O(n) time. O(n) space. BFS.
class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
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
        utils.test(self, __file__, Solution, process_args=utils.root_array_to_tree, process_result=utils.tree_to_array)


if __name__ == '__main__':
    unittest.main()
