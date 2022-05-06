import unittest
from typing import Optional

import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Recursive post-order DFS.
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = -0x80000000

        def dfs(curr):
            if not curr:
                return 0

            left = max(0, dfs(curr.left))
            right = max(0, dfs(curr.right))

            r = left + right + curr.val
            nonlocal result
            if result < r:
                result = r

            return curr.val + max(left, right)

        dfs(root)
        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, process_args=TreeNode.from_root_array)


if __name__ == '__main__':
    unittest.main()
