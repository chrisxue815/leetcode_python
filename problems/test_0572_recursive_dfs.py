import unittest
from typing import Optional

import utils
from tree import TreeNode


def height(root):
    if not root:
        return -1
    return 1 + max(height(root.left), height(root.right))


def match(a, b):
    if not a:
        return not b
    if not b:
        return False
    return a.val == b.val and match(a.left, b.left) and match(a.right, b.right)


# O(n) time. O(log(n)) space. Recursive DFS.
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        subtree_height = height(subRoot)

        def dfs(curr):
            if not curr:
                return False, -1

            left_match, left_height = dfs(curr.left)
            if left_match:
                return True, -1

            right_match, right_height = dfs(curr.right)
            if right_match:
                return True, -1

            curr_height = 1 + max(left_height, right_height)
            if curr_height == subtree_height and match(curr, subRoot):
                return True, -1

            return False, curr_height

        return dfs(root)[0]


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, process_args=self.process_args)

    @staticmethod
    def process_args(args):
        args.root = TreeNode.from_array(args.root)
        args.subRoot = TreeNode.from_array(args.subRoot)


if __name__ == '__main__':
    unittest.main()
