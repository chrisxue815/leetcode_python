import unittest

import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Recursive post-order DFS.
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(curr, depth):
            if not curr:
                return None, depth

            left, left_depth = dfs(curr.left, depth + 1)
            right, right_depth = dfs(curr.right, depth + 1)

            if left_depth == right_depth:
                return curr, left_depth
            if left_depth > right_depth:
                return left, left_depth
            return right, right_depth

        return dfs(root, 0)[0]


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, process_args=TreeNode.from_root_array, process_result=utils.tree_to_array)


if __name__ == '__main__':
    unittest.main()
