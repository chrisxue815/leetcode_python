import unittest

import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Iterative in-order DFS.
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        index = 0
        stack = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            index += 1
            if index == k:
                return root.val
            root = root.right


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, process_args=utils.root_array_to_tree)


if __name__ == '__main__':
    unittest.main()
