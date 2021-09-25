import unittest
from typing import Optional

import utils
from tree import TreeNode


def dfs(node):
    a = node.val  # robbing this node
    b = 0  # not robbing this node

    if node.left:
        la, lb = dfs(node.left)
        a += lb
        b += max(la, lb)

    if node.right:
        ra, rb = dfs(node.right)
        a += rb
        b += max(ra, rb)

    return a, b


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        a, b = dfs(root)
        return max(a, b)


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, process_args=TreeNode.from_root_array)


if __name__ == '__main__':
    unittest.main()
