import unittest

import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Recursive post-order DFS.
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        result = 0

        def dfs(curr):
            if not curr:
                return 2
            left = dfs(curr.left)
            right = dfs(curr.right)
            if left == 0 or right == 0:
                nonlocal result
                result += 1
                return 1
            return 2 if left == 1 or right == 1 else 0

        return (dfs(root) == 0) + result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, process_args=utils.root_array_to_tree)


if __name__ == '__main__':
    unittest.main()
