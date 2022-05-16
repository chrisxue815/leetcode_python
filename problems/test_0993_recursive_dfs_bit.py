import unittest
from typing import Optional

import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Recursive pre-order DFS, bit manipulation.
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        index1 = -1

        def dfs(curr, index):
            if not curr:
                return -1

            if curr.val == x or curr.val == y:
                nonlocal index1
                if index1 == -1:
                    index1 = index
                else:
                    return 1 if index != index1 | 1 and index.bit_length() == index1.bit_length() else 0

            index <<= 1

            left = dfs(curr.left, index)
            if left >= 0:
                return left

            return dfs(curr.right, index + 1)

        return dfs(root, 1) == 1


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, process_args=TreeNode.from_root_array)


if __name__ == '__main__':
    unittest.main()
