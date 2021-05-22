import unittest

import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Recursive post-order DFS.
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def find_deepest(curr):
            if not curr:
                return -1
            return 1 + max(find_deepest(curr.left), find_deepest(curr.right))

        deepest = find_deepest(root)

        def find_result(curr, depth):
            if not curr:
                return None
            if depth >= deepest:
                return curr
            left = find_result(curr.left, depth + 1)
            right = find_result(curr.right, depth + 1)
            return curr if left and right else left or right

        return find_result(root, 0)


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, process_args=utils.root_array_to_tree, process_result=utils.tree_to_array)


if __name__ == '__main__':
    unittest.main()
