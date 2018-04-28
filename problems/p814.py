import unittest
import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Recursive post-order DFS.
class Solution(object):
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
        cases = utils.load_json_from_path('../leetcode_test_cases/p814.json').test_cases

        for case in cases:
            root = TreeNode.from_array(case.root)
            actual = Solution().pruneTree(root)
            actual = TreeNode.to_array_static(actual)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
