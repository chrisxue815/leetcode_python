import unittest
from typing import Optional

import utils
from tree import TreeNode


def kth(node, k, index):
    if not node:
        return index, 0

    index, result = kth(node.left, k, index)
    if index == k:
        return index, result

    index += 1
    if index == k:
        return index, node.val

    return kth(node.right, k, index)


# O(n) time. O(log(n)) space. Recursive in-order DFS.
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return kth(root, k, 0)[1]


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, process_args=TreeNode.from_root_array)


if __name__ == '__main__':
    unittest.main()
