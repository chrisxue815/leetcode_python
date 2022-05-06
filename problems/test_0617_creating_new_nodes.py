import unittest
from typing import Optional

import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Recursive post-order DFS.
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None

        result = TreeNode((root1.val if root1 else 0) + (root2.val if root2 else 0))
        result.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
        result.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)

        return result


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
