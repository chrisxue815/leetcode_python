import unittest

import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Top down, recursive DFS.
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        result = 0

        def dfs(curr, length, is_left):
            nonlocal result
            result = max(result, length)
            if curr.left:
                if is_left:
                    dfs(curr.left, 1, True)
                else:
                    dfs(curr.left, length + 1, True)
            if curr.right:
                if is_left:
                    dfs(curr.right, length + 1, False)
                else:
                    dfs(curr.right, 1, False)

        if root.left:
            dfs(root.left, 1, True)
        if root.right:
            dfs(root.right, 1, False)

        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, process_args=TreeNode.from_root_array)


if __name__ == '__main__':
    unittest.main()
