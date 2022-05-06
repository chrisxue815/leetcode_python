import unittest
from typing import Optional

import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Recursive post-order DFS.
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1

        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, process_args=self.process_args, process_result=self.process_result)

    @staticmethod
    def process_args(case):
        case.root1 = TreeNode.from_array(case.root1)
        case.root2 = TreeNode.from_array(case.root2)

    @staticmethod
    def process_result(actual):
        return TreeNode.to_array_static(actual)


if __name__ == '__main__':
    unittest.main()
