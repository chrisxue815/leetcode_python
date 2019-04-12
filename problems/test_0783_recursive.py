import unittest
import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Recursive in-order traversal.
class Solution(object):
    def __init__(self):
        self.min_diff = 0x7FFFFFFF
        self.prev = None

    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node):
            if not node:
                return
            dfs(node.left)

            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val

            dfs(node.right)

        dfs(root)
        return self.min_diff


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            root = TreeNode.from_array(case.args.root)
            actual = Solution().minDiffInBST(root)
            self.assertEqual(case.expected, actual, msg=case.args)


if __name__ == '__main__':
    unittest.main()
