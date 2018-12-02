import unittest
import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Recursive pre-order DFS.
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def is_same_value(curr, val):
            if not curr:
                return True

            return curr.val == val and is_same_value(curr.left, val) and is_same_value(curr.right, val)

        return is_same_value(root, root.val)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p965.json').test_cases

        for case in cases:
            root = TreeNode.from_array(case.root)
            actual = Solution().isUnivalTree(root)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
