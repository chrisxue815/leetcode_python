import unittest

import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Recursive preorder DFS.
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1

        result = TreeNode(t1.val + t2.val)
        result.left = self.mergeTrees(t1.left, t2.left)
        result.right = self.mergeTrees(t1.right, t2.right)

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            t1 = TreeNode.from_array(case.args.t1)
            t2 = TreeNode.from_array(case.args.t2)
            actual = Solution().mergeTrees(t1, t2)
            actual = actual.to_array()
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
