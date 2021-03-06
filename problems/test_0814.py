import unittest
import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Recursive post-order DFS.
class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def prune(node):
            if not node:
                return True

            left_pruned = prune(node.left)
            if left_pruned:
                node.left = None

            right_pruned = prune(node.right)
            if right_pruned:
                node.right = None

            return left_pruned and right_pruned and node.val == 0

        return None if prune(root) else root


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            root = TreeNode.from_array(case.args.root)
            actual = Solution().pruneTree(root)
            actual = TreeNode.to_array_static(actual)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
