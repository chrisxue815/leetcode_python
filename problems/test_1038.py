import unittest
import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Stack.
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        sum_ = 0

        def dfs(curr):
            nonlocal sum_
            if not curr:
                return 0
            dfs(curr.right)
            sum_ += curr.val
            curr.val = sum_
            dfs(curr.left)

        dfs(root)
        return root


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            root = TreeNode.from_array(case.args.root)
            actual = Solution().bstToGst(root)
            actual = TreeNode.to_array(actual)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
