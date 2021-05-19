import unittest

import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Recursive pre-order DFS.
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0

        result = 0

        if low <= root.val <= high:
            result += root.val
        if low < root.val:
            result += self.rangeSumBST(root.left, low, high)
        if root.val < high:
            result += self.rangeSumBST(root.right, low, high)

        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, process_args=utils.root_array_to_tree)


if __name__ == '__main__':
    unittest.main()
