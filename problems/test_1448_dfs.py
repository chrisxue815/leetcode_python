import unittest

import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Recursive post-order DFS.
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(curr, max_so_far):
            if not curr:
                return 0
            if curr.val >= max_so_far:
                good = 1
                max_so_far = curr.val
            else:
                good = 0
            return good + dfs(curr.left, max_so_far) + dfs(curr.right, max_so_far)

        return dfs(root, -0x80000000)


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, process_args=TreeNode.from_root_array)


if __name__ == '__main__':
    unittest.main()
