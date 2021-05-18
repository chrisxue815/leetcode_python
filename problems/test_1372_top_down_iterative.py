import unittest

import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Top down, iterative DFS.
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        result = 0
        stack = []

        if root.left:
            stack.append((root.left, 1, True))
        if root.right:
            stack.append((root.right, 1, False))

        while stack:
            curr, length, is_left = stack.pop()
            result = max(result, length)
            if curr.left:
                if is_left:
                    stack.append((curr.left, 1, True))
                else:
                    stack.append((curr.left, length + 1, True))
            if curr.right:
                if is_left:
                    stack.append((curr.right, length + 1, False))
                else:
                    stack.append((curr.right, 1, False))

        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, process_args=utils.root_array_to_tree)


if __name__ == '__main__':
    unittest.main()
