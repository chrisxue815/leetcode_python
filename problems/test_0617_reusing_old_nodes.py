import unittest

import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Recursive post-order DFS.
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1

        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1


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
