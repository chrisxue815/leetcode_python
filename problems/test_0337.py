import unittest
from typing import Optional

import utils
from tree import TreeNode


def dfs(node):
    a = 0  # not robbing this node
    b = node.val  # robbing this node
    l = 0
    r = 0

    if node.left:
        l, ll, lr = dfs(node.left)
        a += l
        b += ll + lr

    if node.right:
        r, rl, rr = dfs(node.right)
        a += r
        b += rl + rr

    return max(a, b), l, r


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        result, _, _ = dfs(root)
        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, process_args=TreeNode.from_root_array)


if __name__ == '__main__':
    unittest.main()
