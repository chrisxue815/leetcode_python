import unittest
from typing import Optional

import utils
from tree import TreeNode


def is_symmetric(left, right):
    if left is None:
        return right is None
    if right is None:
        return False
    if left.val != right.val:
        return False
    return is_symmetric(left.left, right.right) and is_symmetric(left.right, right.left)


# O(n) time. O(log(n)) space. Recursive DFS.
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return is_symmetric(root.left, root.right)


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, process_args=TreeNode.from_root_array)


if __name__ == '__main__':
    unittest.main()
