import unittest

import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Recursive pre-order DFS.
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 or not root2:
            return root1 is root2

        if root1.val != root2.val:
            return False

        return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right) or
                self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            root1 = TreeNode.from_array(case.args.root1)
            root2 = TreeNode.from_array(case.args.root2)
            actual = Solution().flipEquiv(root1, root2)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
