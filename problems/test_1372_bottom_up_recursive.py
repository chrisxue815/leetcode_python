import unittest

import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Bottom up, recursive DFS.
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        result = 0

        def dfs(curr):
            if not curr:
                return -1, -1
            ll, lr = dfs(curr.left)
            rl, rr = dfs(curr.right)

            nonlocal result
            result = max(result, ll, rr)

            return lr + 1, rl + 1

        return max(max(dfs(root)), result)


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, process_args=TreeNode.from_root_array)


if __name__ == '__main__':
    unittest.main()
