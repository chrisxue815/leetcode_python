import unittest

import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Recursive post-order DFS, tree height.
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        result = 0

        # Number of nodes in the longest downward path
        def height(curr):
            if not curr:
                return 0

            left_level = height(curr.left)
            right_level = height(curr.right)

            nonlocal result
            result = max(result, left_level + right_level)

            return max(left_level, right_level) + 1

        height(root)

        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, process_args=TreeNode.from_root_array)


if __name__ == '__main__':
    unittest.main()
