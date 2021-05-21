import unittest

import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Recursive post-order DFS.
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return None

        result = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
        result.left = self.mergeTrees(t1.left if t1 else None, t2.left if t2 else None)
        result.right = self.mergeTrees(t1.right if t1 else None, t2.right if t2 else None)

        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, process_args=self.process_args, process_result=self.process_result)

    @staticmethod
    def process_args(case):
        case.t1 = TreeNode.from_array(case.t1)
        case.t2 = TreeNode.from_array(case.t2)

    @staticmethod
    def process_result(actual):
        return TreeNode.to_array_static(actual)


if __name__ == '__main__':
    unittest.main()
