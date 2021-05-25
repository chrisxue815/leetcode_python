import unittest

import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Recursive post-order DFS.
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        result = None
        deepest = 0

        def dfs(curr, depth):
            nonlocal deepest
            if not curr:
                deepest = max(deepest, depth)
                return depth

            left_depth = dfs(curr.left, depth + 1)
            right_depth = dfs(curr.right, depth + 1)

            if left_depth == right_depth:
                if left_depth == deepest:
                    nonlocal result
                    result = curr
                return left_depth

            return max(left_depth, right_depth)

        dfs(root, 0)
        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, process_args=TreeNode.from_root_array, process_result=utils.tree_to_array)


if __name__ == '__main__':
    unittest.main()
