import unittest

import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Recursive pre-order DFS.
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        found = []

        def dfs(curr, parent, depth):
            if not curr:
                return -1

            if curr.val == x or curr.val == y:
                if found:
                    return 1 if found[0] is not parent and found[1] == depth else 0
                else:
                    found[:] = [parent, depth]

            left = dfs(curr.left, curr, depth + 1)
            if left >= 0:
                return left

            return dfs(curr.right, curr, depth + 1)

        return dfs(root, None, 0) == 1


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, process_args=TreeNode.from_root_array)


if __name__ == '__main__':
    unittest.main()
